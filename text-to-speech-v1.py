import openai
import json

def load_api_key():
    with open('config.json', 'r') as config_file:
        config = json.load(config_file)
        return config['OPENAI_API_KEY']

def generate_audio(text):
    openai.api_key = load_api_key()

    response = openai.Audio.create(
        model="text-to-speech",
        input=text,
        voice="pt-BR-Standard-A",
        language="pt-BR"
    )

    return response["url"]

if __name__ == "__main__":
    text = input("Enter the text to be spoken: ")
    audio_url = generate_audio(text)
    print(f"Audio URL: {audio_url}")
