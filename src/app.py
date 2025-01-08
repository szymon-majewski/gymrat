from instagram_uploader import upload_image_to_instagram
from dropbox_uploader import upload_to_dropbox
from ai_generator import generate_text, generate_image

text_prompt = "Write a short, motivational text for an instagram post about starting out with excercising at the gym."
image_prompt = "An european and motivated female teenager excercising at the gym for the first time."
image_path = "gym_3.png"

instagram_caption = generate_text(text_prompt)
generate_image(image_prompt, image_path)
image_dropbox_link = upload_to_dropbox(image_path, f"/gymrat/{image_path}")
upload_image_to_instagram(image_dropbox_link, instagram_caption)
