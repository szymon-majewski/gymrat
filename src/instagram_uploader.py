import requests
import os
from dotenv import load_dotenv

load_dotenv()
ACCESS_TOKEN = os.getenv("INSTAGRAM_ACCESS_TOKEN")
ACCOUNT_ID = os.getenv("INSTAGRAM_ACCOUNT_ID")


def upload_image_to_instagram(image_path, caption):
    media_url = f"https://graph.facebook.com/v12.0/{ACCOUNT_ID}/media"
    image_data = {
        "image_url": image_path,
        "caption": caption,
        "access_token": ACCESS_TOKEN,
    }
    response = requests.post(media_url, data=image_data)
    media_id = response.json().get("id")

    if not media_id:
        print(f"Error uploading media: {response.json()}")
        return None

    publish_url = f"https://graph.facebook.com/v12.0/{ACCOUNT_ID}/media_publish"
    publish_data = {
        "creation_id": media_id,
        "access_token": ACCESS_TOKEN,
    }
    publish_response = requests.post(publish_url, data=publish_data)
    if publish_response.status_code == 200:
        print("Post published successfully!")
    else:
        print(f"Error publishing post: {publish_response.json()}")
