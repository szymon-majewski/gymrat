import dropbox
import os
from dotenv import load_dotenv

load_dotenv()
APP_KEY = os.getenv("DROPBOX_APP_KEY")
APP_SECRET = os.getenv("DROPBOX_APP_SECRET")
REFRESH_TOKEN = os.getenv("DROPBOX_REFRESH_TOKEN")


def upload_to_dropbox(file_path, target_path):
    dbx = dropbox.Dropbox(
        oauth2_refresh_token=REFRESH_TOKEN,
        app_key=APP_KEY,
        app_secret=APP_SECRET
    )

    with open(file_path, "rb") as file:
        dbx.files_upload(file.read(), target_path, mode=dropbox.files.WriteMode("overwrite"))

    shared_link_metadata = dbx.sharing_create_shared_link_with_settings(target_path)
    direct_link = shared_link_metadata.url.replace("&dl=0", "&raw=1")
    return direct_link
