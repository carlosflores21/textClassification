# Text Classification with Toxicity Analysis
This project is a web application for text classification and toxicity analysis using machine learning models. The application leverages `DistilBERT` and `RoBERTa` models for the analysis, providing functionalities such as text cleaning, language support, and text perturbations.


## Requirements
```text
 • transformers
 • torch
 • pandas
 • numpy<2
 • sentencepiece
 • flask
 • langdetect
 • spacy
 • googletrans==4.0.0-rc1
```
## Installation
1. Clone the repository:

    ```bash
    git clone https://github.com/carlosflores21/textClassification.git
    cd textClassification
    ```
2. Create and activate a virtual environment:

    ```bash
    python -m venv .venv
    .venv\Scripts\activate
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Download and place the pre-trained models in the `models` directory.

   - [DistilBERT Model](https://www.kaggle.com/code/charlyj21/db-sixcat/output)
   - [RoBERTa Model](https://www.kaggle.com/code/charlyj21/rb-sixcat/output)

## Usage

1. Run the Flask application:

    ```bash
    python app.py
    ```

2. Open your web browser and go to `http://127.0.0.1:5000`.

3. Enter the text you want to analyze, adjust the configurations, and click "Evaluate".

## Project Structure
- `functions/`: Directory containing helper functions for text processing.
- `models/`: Directory containing trained models.
- `static/`: Directory containing static files (CSS, JS).
- `templates/`: Directory containing HTML templates.
- `app.py`: Main application file.
- `requirements.txt`: List of Python dependencies.


## Features

- **Text Cleaning**: Perform lemmatization using spaCy models.
- **Language Support**: Detect and translate text to English for analysis.
- **Text Perturbations**: Handle common text perturbations like character replacements.
- **Toxicity Analysis**: Analyze the text for different toxicity labels using `DistilBERT` and `RoBERTa` models.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author

This project was developed by [Carlos Flores](https://github.com/carlosflores21).