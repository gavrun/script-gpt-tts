import json
from pathlib import Path
from openai import OpenAI

def load_api_key():
    with open('config.json', 'r') as config_file:
        config = json.load(config_file)
        return config['OPENAI_API_KEY']
    
client = OpenAI(
    api_key=load_api_key(),
)

speech_file_path = Path(__file__).parent / "speech.mp3"
response = client.audio.speech.create(
  model="tts-1",
  voice="alloy",
  input=input("Enter the text in Portuguese: ")
)

response.stream_to_file(speech_file_path)
