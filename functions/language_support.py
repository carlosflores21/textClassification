from googletrans import Translator
from langdetect import detect

def detect_language(text):
    try:
        return detect(text)
    except:
        return 'unknown'
def translate(text):
    try:
        translator = Translator()
        translation = translator.translate(text, dest='en')
        return translation.text
    except Exception as e:
        print(f"Translation error: {e}")
        return text

def process_text(text, function2=False):
    if function2:
        if text == '':
            return text
        # Detectar el idioma del texto
        lang = detect_language(text)
        print(f"Detected language: {lang}")

        # Si el idioma no es ingles, traducir al inglés
        if lang != 'en':
            translated_text = translate(text)
            print(f"Translated text: {translated_text}")
            return translated_text
        else:
            # Si es ingles, devolver el texto original
            return text
    return text