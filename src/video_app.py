from ai_generator import generate_text, generate_image
from tts import generate_audio
from video_maker import generate_video
from datetime import datetime
import os

num_images = 7
topic = "benefits of weighted squats"
topic_with_underscores = topic.replace(" ", "_")

text_prompt = f"Write a short, motivational text for an instagram post about the {topic}."
read_text_prompt = f"Write a short, motivational text about the {topic} that will be used as a voiceover in an instagram video. Write only the text that will be read."
images_generation_prompts = (
    f"Generate {num_images} diverse and detailed image prompts for a gym-related Instagram video. "
    f"The prompts should feature people and be related to the topic \"{topic}\". The descriptions should specify diversity "
    f"in gender, ethnicity, and setting (e.g. gym, outdoor). Example format: '<Description of person> <Action related to the topic> <location>'. "
    f"Separate the prompts with new line characters."
)

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
base_path = f"{topic_with_underscores}_{timestamp}"
audio_path = f"generations/{base_path}/{base_path}.mp3"
video_path = f"generations/{base_path}/{base_path}.mp4"
os.mkdir(f"generations/{base_path}")

print(f"Path to media: {base_path}")

instagram_caption = generate_text(text_prompt)
with open("reflinks.txt", 'r') as reflinks_file:
    reflinks = reflinks_file.read()
    instagram_caption = f'{instagram_caption}\n{reflinks}'
with open(f"generations/{base_path}/caption.txt", 'w') as caption_file:
    caption_file.write(instagram_caption)

# read_text = generate_text(read_text_prompt).split("#")[0] + " Check out the description for more info on the topic!"
# with open(f"generations/{base_path}/read_text.txt", 'w') as read_text_file:
#     read_text_file.write(read_text)
# 
# caption_audio = generate_audio(read_text, audio_path)
# 
# raw_image_prompts = generate_text(images_generation_prompts).split("\n")
# image_prompts = []
# for i, prompt in enumerate(raw_image_prompts):
#     if i % 2 == 0:
#         image_prompt = prompt.split(" ", 1)[-1]
#         image_prompts.append(image_prompt)
# with open(f"generations/{base_path}/image_prompts.txt", 'w') as image_prompts_file:
#     for prompt in image_prompts:
#         image_prompts_file.write(f"{prompt}\n")
# 
# assert len(image_prompts) == num_images
# images_paths = []
# for i, image_prompt in enumerate(image_prompts):
#     image_path = f"generations/{base_path}/{base_path}_{i}.png"
#     images_paths.append(image_path)
#     try:
#         generate_image(image_prompt, image_path)
#     except Exception as error:
#         print("An error occured while generating image:", error)
# 
# generate_video(images_paths, audio_path, video_path)
