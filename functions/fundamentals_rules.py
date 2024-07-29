import re

def fundamentals(text):
    # Eliminar espacios en blanco adicionales
    text = text.strip()
    # URLs
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    return text