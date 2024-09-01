# Language Detection and Translation Flask App
![Language Detection & Translation](https://img.shields.io/badge/Language%20Detection%20%26%20Translation-Python%20%7C%20Flask%20%7C%20langdetect%20%7C%20googletrans-brightgreen)


This is a Flask application that detects the language of input text and translates it into a target language using `langdetect` and `googletrans` libraries. The application also utilizes `Flask-Caching` for improved performance by caching the results of language detection and translation.


![Language Detection and Translation Flask App Dashboard](https://github.com/omspatil/Language-Detection-and-Translation/blob/453579c066f5ae26b92a40c4aec2b7ec4bd3696a/Language%20Detection%20and%20Translation/Images/Dashboard.png)


## Features

- **Language Detection:** Detects the language of the input text.
- **Translation:** Translates the detected language into a user-selected target language.
- **Caching:** Caches the results of language detection and translation for improved performance.
- **Responsive UI:** User-friendly interface with Bootstrap and custom CSS animations.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/language-translation-app.git
    ```

2. Navigate to the project directory:
    ```bash
    cd language-translation-app
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the application:
    ```bash
    python app.py
    ```

## Usage

1. Enter the text you want to detect and translate into the input field.
2. Select the target language from the dropdown menu.
3. Click the "Translate" button to view the detected language and its translation.

## Dependencies

- Flask
- langdetect
- googletrans
- Flask-Caching
- Bootstrap (for UI)

## Acknowledgments

This project uses the following libraries:
- [Flask](https://flask.palletsprojects.com/)
- [langdetect](https://pypi.org/project/langdetect/)
- [googletrans](https://pypi.org/project/googletrans/)
- [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/)

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss your ideas.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## File Structure

```bash
.
├── app.py              # Main Flask application
├── templates
│   └── index.html      # HTML template for the home page
├── static
│   ├── style.css       # Custom CSS for styling (if needed)
└── requirements.txt    # Python dependencies
