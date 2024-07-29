from flask import Flask, request, render_template, redirect, url_for
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification, XLMRobertaTokenizer, \
    XLMRobertaForSequenceClassification
import torch
from functions.clean_text import clean
from functions.language_support import process_text
from functions.perturbations import format
from functions.fundamentals_rules import fundamentals
import json

app = Flask(__name__)

# Ruta de los modelos
model_path_DT = "models/trained_model_SC_DT"
model_path_RB = "models/trained_model_SC_RB"

# Cargar tokenizers y modelos
tokenizer_DT = DistilBertTokenizer.from_pretrained(model_path_DT)
model_DT = DistilBertForSequenceClassification.from_pretrained(model_path_DT)

tokenizer_RB = XLMRobertaTokenizer.from_pretrained(model_path_RB)
model_RB = XLMRobertaForSequenceClassification.from_pretrained(model_path_RB)

# Dispositivo local
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model_DT.to(device)
model_RB.to(device)


@app.route('/', methods=['GET', 'POST'])
def index():
    function1 = False
    function2 = True
    function3 = True
    function4 = False
    function5 = False
    function6 = False
    level = 5

    predictions_DT = {}
    predictions_RB = {}

    if request.method == 'POST':
        text = request.form['text']
        text_origin = text
        function1 = request.form.get('function1') == 'true'
        function2 = request.form.get('function2') == 'true'
        function3 = request.form.get('function3') == 'true'
        function4 = request.form.get('function4') == 'true'
        function5 = request.form.get('function5') == 'true'
        function6 = request.form.get('function6') == 'true'
        level = int(request.form['level'])

        # Fundamentals
        text = fundamentals(text)
        print("Fundamentals: "+ text)
        # Perturbations
        if function3:
            text = format(text, function3=function3)
            print("Perturbation result: " + text)
        # Aplicar limpieza si function1 está activada
        if function1:
            text = clean(text, function1=function1)
            print("Clean text result: "+text)
        # Traducir si function2 está activada
        if function2:
            text = process_text(text, function2=function2)
            print("Translate text result: " + text)

        predictions_DT = predict(text, model_DT, tokenizer_DT, level)
        predictions_RB = predict(text, model_RB, tokenizer_RB, level)
        return redirect(url_for('index', text=text_origin,
                                predictions_DT=json.dumps(predictions_DT),
                                predictions_RB=json.dumps(predictions_RB),
                                function1=str(function1).lower(), function2=str(function2).lower(),
                                function3=str(function3).lower(),
                                function4=str(function4).lower(), function5=str(function5).lower(),
                                function6=str(function6).lower(),
                                level=level))
    text = request.args.get('text', '')
    predictions_DT = request.args.get('predictions_DT')
    predictions_RB = request.args.get('predictions_RB')
    function1 = request.args.get('function1', 'false') == 'true'
    function2 = request.args.get('function2', 'true') == 'true'
    function3 = request.args.get('function3', 'true') == 'true'
    function4 = request.args.get('function4', 'false') == 'true'
    function5 = request.args.get('function5', 'false') == 'true'
    function6 = request.args.get('function6', 'false') == 'true'
    level = int(request.args.get('level', 5))

    if predictions_DT:
        try:
            predictions_DT = json.loads(predictions_DT.replace("'", "\""))
        except json.JSONDecodeError as e:
            print(f"Error decoding predictions_DT: {e}")
            predictions_DT = {}
    if predictions_RB:
        try:
            predictions_RB = json.loads(predictions_RB.replace("'", "\""))
        except json.JSONDecodeError as e:
            print(f"Error decoding predictions_RB: {e}")
            predictions_RB = {}


    return render_template('index.html', text=text,
                           predictions_DT=predictions_DT,
                           predictions_RB=predictions_RB,
                           function1=function1, function2=function2, function3=function3,
                           function4=function4, function5=function5, function6=function6,
                           level=level)


def predict(text, model, tokenizer, threshold):
    # Tokenizar el texto
    inputs = tokenizer([text], padding=True, truncation=True, return_tensors="pt", max_length=128)
    inputs = {key: value.to(device) for key, value in inputs.items()}

    # Poner el modelo en modo evaluación
    model.eval()

    # Desactivar el cálculo de gradientes para hacer las predicciones
    with torch.no_grad():
        outputs = model(**inputs)

    # Obtener las predicciones
    predictions = torch.sigmoid(outputs.logits).cpu().numpy()

    threshold_float = threshold/10
    # Umbrales de decisión por categoría
    thresholds = [threshold_float, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]

    # Convertir probabilidades a etiquetas binarias con los nuevos umbrales
    binary_predictions = (predictions >= thresholds).astype(int)

    # Etiquetas correspondientes a cada categoría
    labels = ['target', 'severe_toxicity', 'obscene', 'identity_attack', 'insult', 'threat', 'sexual_explicit']

    # Crear un diccionario de predicciones
    results = {label: {'value': int(pred), 'probability': float(prob)} for label, pred, prob in
               zip(labels, binary_predictions[0], predictions[0])}

    return results


if __name__ == '__main__':
    app.run(debug=True)
