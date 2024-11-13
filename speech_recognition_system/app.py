from flask import Flask, render_template, request, jsonify
from googletrans import Translator
import speech_recognition as sr
from gtts import gTTS
import os

app = Flask(__name__)
translator = Translator()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    data = request.get_json()
    text = data['text']
    lang = data['language']
    translation = translator.translate(text, dest=lang)
    return jsonify({"translated_text": translation.text})

@app.route('/speech-to-text', methods=['POST'])
def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        return jsonify({"text": text})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
