from instagram_uploader import upload_video_to_instagram
from dropbox_uploader import upload_to_dropbox
import subprocess


def resize_video_with_ffmpeg(input_path, output_path):
    ffmpeg_command = [
        'ffmpeg',
        '-i', input_path,
        '-vf', 'crop=min(iw\\,ih):min(iw\\,ih),scale=1080:1080',
        '-c:a', 'copy',
        output_path
    ]

    try:
        subprocess.run(ffmpeg_command, check=True)
        print(f"Video resized successfully: {output_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error resizing video: {e}")


base_path = input('Enter base path of media: ')

with open(f'generations/{base_path}/caption.txt', 'r') as caption_file:
    instagram_caption = caption_file.read()

resize_video_with_ffmpeg(f'generations/{base_path}/{base_path}_sub.mp4', f'generations/{base_path}/{base_path}_sub_crop.mp4')

image_dropbox_link = upload_to_dropbox(f"generations/{base_path}/{base_path}_sub_crop.mp4", f"/gymrat/{base_path}_sub_crop.mp4")
upload_video_to_instagram(image_dropbox_link, instagram_caption)
