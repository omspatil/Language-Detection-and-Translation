from flask import Flask, render_template, request, flash
from langdetect import detect, LangDetectException
from googletrans import Translator, LANGUAGES
import threading
import functools
from flask_caching import Cache

# Create a Flask application instance
app = Flask(__name__)

# Secret key required for flashing messages (e.g., error messages)
app.secret_key = 'your_secret_key_here'

# Configure cache
cache = Cache(app, config={'CACHE_TYPE': 'simple'})

# Create a Translator object once
translator = Translator()

def cached_translation(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Create a cache key based on input arguments
        cache_key = f"{args}-{kwargs}"
        # Try to get the result from the cache
        cached_result = cache.get(cache_key)
        if cached_result:
            return cached_result
        # If not cached, call the function and store the result
        result = func(*args, **kwargs)
        cache.set(cache_key, result, timeout=5*60)  # Cache for 5 minutes
        return result
    return wrapper

@cached_translation
def detect_and_translate(text, target_lang):
    try:
        # Detect the language of the input text
        detected_lang_code = detect(text)
        detected_lang = LANGUAGES.get(detected_lang_code, 'Unknown')
    except LangDetectException:
        # Return None if language detection fails
        return None, None

    # Translate the text to the target language
    translated_text = translator.translate(text, dest=target_lang).text

    # Return the full name of the detected language and translated text
    return detected_lang, translated_text

@app.route('/')
def index():
    return render_template('index.html', languages=LANGUAGES)

@app.route('/trans', methods=['POST'])
def trans():
    translation = ""
    detected_lang = ""

    text = request.form.get('text')
    target_lang = request.form.get('target_lang')

    if not text or not target_lang:
        flash('Please provide both text and a target language.', 'error')
        return render_template('index.html', languages=LANGUAGES)

    # Perform language detection and translation asynchronously
    thread = threading.Thread(target=lambda: detect_and_translate(text, target_lang))
    thread.start()
    thread.join()

    detected_lang, translation = detect_and_translate(text, target_lang)

    if detected_lang is None:
        flash('Language detection failed. Please try again with a different text.', 'error')
        return render_template('index.html', languages=LANGUAGES)

    return render_template('index.html', translation=translation, detected_lang=detected_lang, languages=LANGUAGES)

if __name__ == '__main__':
    app.run(debug=True)
