from instagram_uploader import upload_image_to_instagram
from dropbox_uploader import upload_to_dropbox
from ai_generator import generate_text, generate_image
from datetime import datetime

text_prompt = "Write a short text for an instagram post about the topic \"Health is happiness\". Generally something like going to gym gives you good health, and health gives you happiness."
image_prompt = "A Caucasian teenager, engrossed in her music, sprinting on a quiet beach at sunrise. The waves crash softly in the background, and her ponytail sways with each stride as she embraces the tranquility of her surroundings."
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
base_path = f"jogging_{timestamp}"
image_path = f"{base_path}.png"

instagram_caption = generate_text(text_prompt)
generate_image(image_prompt, image_path)
image_dropbox_link = upload_to_dropbox(image_path, f"/gymrat/{image_path}")
upload_image_to_instagram(image_dropbox_link, instagram_caption)
