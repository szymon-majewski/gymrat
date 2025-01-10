import requests
import os
from dotenv import load_dotenv

load_dotenv()
ACCESS_TOKEN = os.getenv("ELEVENLABS_ACCESS_TOKEN")
brian_voice_id = 'nPczCjzI2devNBz1zQrb'


def generate_audio(text, audio_path, voice_id=brian_voice_id):
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
    headers = {
        "Content-Type": "application/json",
        "xi-api-key": ACCESS_TOKEN,
    }
    data = {
        "text": text,
        "voice_settings": {
            "stability": 0.75,
            "similarity_boost": 0.85
        }
    }

    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 200:
        with open(audio_path, "wb") as f:
            f.write(response.content)
    else:
        print(f"error: {response.status_code}, {response.text}")
        raise Exception("Failed to generate audio")
