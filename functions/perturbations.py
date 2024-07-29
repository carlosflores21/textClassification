import re

def format(text, function3=False):
    if function3:
        # Eliminar repetidos
        text = re.sub(r'(.)\1{2,}', r'\1', text)
        # Minuscula
        text.lower()
        # Reemplazar
        replacements = {
            '@': 'a',
            '1': 'i',
            '0': 'o',
            '4': 'a',
            '3': 'e',
            '$': 's',
            '7': 't',
            '5': 's',
            '2': 'z',
            '9': 'g',
            '8': 'b',
            '|': 'l',
            '+': 't'
        }
        for special, original in replacements.items():
            text = text.replace(special, original)
        # Eliminar puntuación
        text = re.sub(r'[^\w\s]', '', text)
        # Eliminar caracteres especiales
        text = re.sub(r'[^\x00-\x7F]+', '', text)
        return text
    return text