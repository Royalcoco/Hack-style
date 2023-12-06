import json

def read_data_from_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def translate_text(text, target_language):
    """Translates text from English to French."""
    translate_client = translate.Client()

    result = translate_client.translate(
        text, target_language=target_language)

    return result['translatedText']

# Set your JSON file path
json_file_path = 'your_file_path.json'

# Read the data from the JSON file:
data = read_data_from_json_file(json_file_path)

# Set the target language
target_language = 'fr'

# Translate the text
translated_text = translate_text(data['text'], target_language)

print(f"Translated text: {translated_text}")

from transformers import pipeline

def translate_text(text, target_language):
    translator = pipeline('translation_en_to_fr', model='t5-small')
    translated_text = translator(text)[0]['translation_text']
    return translated_text