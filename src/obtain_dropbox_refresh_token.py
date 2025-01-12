import dropbox
import os
from dotenv import load_dotenv

load_dotenv()
APP_KEY = os.getenv("DROPBOX_APP_KEY")
APP_SECRET = os.getenv("DROPBOX_APP_SECRET")

auth_flow = dropbox.DropboxOAuth2FlowNoRedirect(
    APP_KEY, APP_SECRET, use_pkce=True, token_access_type="offline"
)
authorize_url = auth_flow.start()
print("1. Go to: " + authorize_url)
print("2. Click 'Allow' (you might have to log in first).")
print("3. Copy the authorization code.")

auth_code = input("Enter the authorization code here: ").strip()
token_result = auth_flow.finish(auth_code)

print("Access token:", token_result.access_token)
print("Refresh token:", getattr(token_result, 'refresh_token', 'No refresh token received'))
