from instagram_uploader import upload_image_to_instagram
from dropbox_uploader import upload_to_dropbox
from ai_generator import generate_text, generate_image
from tts import generate_audio
from video_maker import generate_video
from datetime import datetime

num_images = 6
text_prompt = "Write a short, motivational text for an instagram post about the benefits of running."
read_text_prompt = "Write a short, motivational text about the benefits of running that will be used as a voiceover in an instagram video. Write only the text that will be read."
images_generation_prompts = (
    f"Generate {num_images} diverse and detailed image prompts for a gym-related Instagram video. "
    f"The prompts should feature people running on a treadmill or running outdoors, and the descriptions should specify diversity "
    f"in gender, ethnicity, and setting (e.g. gym, outdoor). Example format: '<Description of person> running <location>'."
    f"Separate the prompts with new line characters."
)
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
base_path = f"jogging_{timestamp}"
audio_path = f"{base_path}.mp3"
video_path = f"{base_path}.mp4"

instagram_caption = generate_text(text_prompt)
print(instagram_caption)

read_text = generate_text(read_text_prompt).split("#")[0] + " Check out the description for more info on the topic!"
print(read_text)

caption_audio = generate_audio(read_text, audio_path)

raw_image_prompts = generate_text(images_generation_prompts).split("\n")
image_prompts = []
for i, prompt in enumerate(raw_image_prompts):
    if i % 2 == 0:
        image_prompt = prompt.split(" ", 1)[-1]
        image_prompts.append(image_prompt)
print(image_prompts)
assert len(image_prompts) == num_images
images_paths = []
for i, image_prompt in enumerate(image_prompts):
    image_path = f"{base_path}_{i}.png"
    images_paths.append(image_path)
    generate_image(image_prompt, image_path)

generate_video(images_paths, audio_path, video_path)

# image_dropbox_link = upload_to_dropbox(image_path, f"/gymrat/{image_path}")
# upload_image_to_instagram(image_dropbox_link, instagram_caption)
