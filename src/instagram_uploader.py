import requests
import os
import time
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


def upload_video_to_instagram(video_url, caption):
    media_url = f"https://graph.facebook.com/v12.0/{ACCOUNT_ID}/media"
    video_data = {
        "video_url": video_url,
        "caption": caption,
        "media_type": "REELS",
        "access_token": ACCESS_TOKEN,
    }

    response = requests.post(media_url, data=video_data)
    response_json = response.json()

    if "id" not in response_json:
        print(f"Error uploading video: {response_json}")
        return None

    media_id = response_json["id"]
    print(f"Video uploaded, media ID: {media_id}")

    while True:
        status_url = f"https://graph.facebook.com/v12.0/{media_id}?fields=status_code&access_token={ACCESS_TOKEN}"
        status_response = requests.get(status_url)
        status_json = status_response.json()

        if status_json.get("status_code") == "FINISHED":
            break
        elif status_json.get("status_code") == "ERROR":
            print("Error processing video")
            return None
        time.sleep(1)

    publish_url = f"https://graph.facebook.com/v12.0/{ACCOUNT_ID}/media_publish"
    publish_data = {
        "creation_id": media_id,
        "access_token": ACCESS_TOKEN,
    }
    publish_response = requests.post(publish_url, data=publish_data)

    if publish_response.status_code == 200:
        print("Video published successfully!")
    else:
        print(f"Error publishing video: {publish_response.json()}")
