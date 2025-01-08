import requests
import os
from dotenv import load_dotenv

load_dotenv()
CLIENT_ID = os.getenv("IMGUR_CLIENT_ID")


def upload_to_imgur(image_path):
    headers = {"Authorization": f"Client-ID {CLIENT_ID}"}
    with open(image_path, "rb") as image_file:
        files = {"image": image_file}
        response = requests.post("https://api.imgur.com/3/upload", headers=headers, files=files)

    print(f"Response status code: {response.status_code}")
    print(f"Response content: {response.text}")

    if response.status_code == 200:
        return response.json()["data"]["link"]
    else:
        raise Exception(f"Error uploading to Imgur: {response.json()}")
