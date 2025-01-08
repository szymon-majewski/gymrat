import dropbox
import os
from dotenv import load_dotenv

load_dotenv()
ACCESS_TOKEN = os.getenv("DROPBOX_ACCESS_TOKEN")


def upload_to_dropbox(file_path, target_path):
    dbx = dropbox.Dropbox(ACCESS_TOKEN)

    with open(file_path, "rb") as file:
        dbx.files_upload(file.read(), target_path, mode=dropbox.files.WriteMode("overwrite"))

    shared_link_metadata = dbx.sharing_create_shared_link_with_settings(target_path)
    direct_link = shared_link_metadata.url.replace("&dl=0", "&raw=1")
    return direct_link
