from langdetect import detect
import spacy

# Cargar los modelos de spaCy
spacy_models = {
    'en': spacy.load('en_core_web_sm'),
    'es': spacy.load('es_core_news_sm'),
    # Agrega otros modelos aquí
}

def detect_language(text):
    try:
        return detect(text)
    except:
        return 'unknown'

def clean(text, function1=False):
    if function1:
        lang = detect_language(text)
        if lang in spacy_models:
            nlp = spacy_models[lang]
        else:
            nlp = spacy_models['en']  # Por defecto, usa el modelo en inglés si el idioma no es soportado

        # Procesar el texto con spaCy
        doc = nlp(text)

        # Realizar lematización
        cleaned_tokens = [token.lemma_ for token in doc]

        # Unir tokens limpios en una cadena
        text = ' '.join(cleaned_tokens)
    return text