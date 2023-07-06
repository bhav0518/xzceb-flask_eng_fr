from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator", template_folder="templates")

@app.route("/", methods = ['GET'])
def renderIndexPage():
    return render_template('index.html')

@app.route("/englishToFrench", methods=['GET', 'POST'])
def english_to_french_endpoint():
    english_text = request.args.get('textToTranslate')
    french_translation = translator.english_to_french(english_text)
    return french_translation

@app.route("/frenchToEnglish", methods=['GET', 'POST'])
def french_to_english_endpoint():
    french_text = request.args.get('textToTranslate')
    english_translation = translator.french_to_english(french_text)
    return english_translation

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
