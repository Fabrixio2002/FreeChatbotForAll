from flask import Flask, render_template, jsonify, request, send_from_directory
import json
from nltk.chat.util import Chat, reflections
import nltk
import re
import unicodedata
import os

# Descargar los recursos necesarios de NLTK
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

app = Flask(__name__)

def normalize_text(text):
    # Convertir el texto a minúsculas
    text = text.lower()
    
    # Eliminar acentos
    text = ''.join(
        (c for c in unicodedata.normalize('NFD', text)
         if unicodedata.category(c) != 'Mn')
    )
    
    # Eliminar signos de interrogación y otros signos de puntuación
    text = re.sub(r'[¿?¡!.,;]', '', text)
    
    return text

# Cargar el archivo JSON
with open('intents.json', 'r', encoding='utf-8') as file:
    intents = json.load(file)

# Transformar los datos del JSON en pares para el chatbot
pares = []
for intent in intents['intents']:
    for pattern in intent['patterns']:
        normalized_pattern = normalize_text(pattern)
        pares.append((normalized_pattern, intent['responses']))

# Crear el chatbot
chatbot = Chat(pares, reflections)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

@app.route('/mensaje', methods=['POST'])
def mensaje():
    user_message = request.form['mensaje']
    normalized_message = normalize_text(user_message)
    bot_response = chatbot.respond(normalized_message)
    
    if not bot_response:
        bot_response = "Lo siento, no entiendo tu mensaje. ¿Podrías reformularlo?"

    response_type = 'text'
    if bot_response:
        for resp in bot_response.split():
            if resp.startswith('documentos/'):
                response_type = 'pdf'
                break

    return jsonify({'respuesta': bot_response, 'type': response_type})

@app.route('/documentos/<path:filename>')
def send_pdf(filename):
    return send_from_directory('documentos', filename)

@app.route('/enviar_pregunta', methods=['POST'])
def enviar_pregunta():
    new_question = request.form['pregunta']
    tag = "pregunta_frecuente"
    
    # Normalizar la pregunta
    normalized_question = normalize_text(new_question)
    
    # Cargar el archivo JSON
    with open('intents.json', 'r', encoding='utf-8') as file:
        intents = json.load(file)
    
    # Buscar si ya existe el tag de preguntas frecuentes
    for intent in intents['intents']:
        if intent['tag'] == tag:
            intent['patterns'].append(normalized_question)
            break
    else:
        # Si no existe, agregar una nueva intención
        intents['intents'].append({
            'tag': tag,
            'patterns': [normalized_question],
            'responses': []
        })
    
    # Guardar los cambios en el archivo JSON
    with open('intents.json', 'w', encoding='utf-8') as file:
        json.dump(intents, file, ensure_ascii=False, indent=4)
    
    return jsonify({'status': 'success', 'message': 'Pregunta enviada con éxito'})

@app.route('/obtener_preguntas_sin_respuesta')
def obtener_preguntas_sin_respuesta():
    # Cargar el archivo JSON
    with open('intents.json', 'r', encoding='utf-8') as file:
        intents = json.load(file)
    
    preguntas_sin_respuesta = []
    for intent in intents['intents']:
        if intent['tag'] == "pregunta_frecuente" and not intent['responses']:
            preguntas_sin_respuesta.extend(intent['patterns'])
    
    return jsonify({'preguntas': preguntas_sin_respuesta})

@app.route('/agregar_respuesta', methods=['POST'])
def agregar_respuesta():
    pregunta = request.form['pregunta']
    respuesta = request.form['respuesta']
    
    # Normalizar la pregunta
    normalized_pregunta = normalize_text(pregunta)
    
    # Cargar el archivo JSON
    with open('intents.json', 'r', encoding='utf-8') as file:
        intents = json.load(file)
    
    # Agregar la respuesta a la pregunta correspondiente
    for intent in intents['intents']:
        if normalized_pregunta in intent['patterns']:
            intent['responses'].append(respuesta)
            break
    
    # Guardar los cambios en el archivo JSON
    with open('intents.json', 'w', encoding='utf-8') as file:
        json.dump(intents, file, ensure_ascii=False, indent=4)
    
    return jsonify({'status': 'success', 'message': 'Respuesta agregada con éxito'})

@app.route('/admin')
def admin():
    return render_template('admin.html')

if __name__ == '__main__':
    app.run(debug=True)
