from instagram_uploader import upload_image_to_instagram
from dropbox_uploader import upload_to_dropbox
from ai_generator import generate_text, generate_image
from tts import generate_audio
from video_maker import generate_video

text_prompt = "Write a short, motivational text for an instagram post about the benefits of doing pull-ups."
read_text_prompt = "Write a short, motivational text about the benefits of doing pull-ups that will be used as a voiceover in an instagram video. Write only the text that will be read."
image_prompts = [
    "An european and naturally looking, young woman with a gentle smile performing a pull-up exercise at the gym.",
    "A black and naturally looking young man performing a pull-up exercise at the gym.",
    "A black, young, naturally looking man with a gentle smile performing a pull-up exercise at the outdoor gym.",
    "An asian female teenager performing a pull-up exercise at the gym.",
    "An european and naturally looking young man performing a pull-up exercise at the outdoor gym.",
]
base_path = "pullup_benefits"
audio_path = f"{base_path}.mp3"
video_path = f"{base_path}.mp4"

instagram_caption = generate_text(text_prompt)
with open('caption_for_final_video.txt', 'w') as file:
    file.write(instagram_caption)

read_text = generate_text(read_text_prompt).split("#")[0] + " Check out the description for more info on the topic!"
caption_audio = generate_audio(read_text, audio_path)
images_paths = []
for i, image_prompt in enumerate(image_prompts):
    image_path = f"{base_path}_{i}.png"
    images_paths.append(image_path)
    generate_image(image_prompt, image_path)

generate_video(images_paths, audio_path, video_path)

image_dropbox_link = upload_to_dropbox(image_path, f"/gymrat/{image_path}")
upload_image_to_instagram(image_dropbox_link, instagram_caption)
