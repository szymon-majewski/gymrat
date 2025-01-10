from instagram_uploader import upload_image_to_instagram
from dropbox_uploader import upload_to_dropbox
from ai_generator import generate_text, generate_image

text_prompt = "Write a short text for an instagram post, in which you encourage people above 40 years old to start exercising at the gym."
image_prompt = "A naturally looking, middle-aged man exercising at the gym."
base_path = "older_1"
image_path = f"{base_path}.png"

instagram_caption = generate_text(text_prompt)
generate_image(image_prompt, image_path)
image_dropbox_link = upload_to_dropbox(image_path, f"/gymrat/{image_path}")
upload_image_to_instagram(image_dropbox_link, instagram_caption)
