from moviepy import ImageClip, AudioFileClip, concatenate_videoclips
from pydub import AudioSegment


def generate_video(images_paths, audio_path, output_path):
    clips = []
    audio = AudioSegment.from_file(audio_path)
    duration_per_image = len(audio) / len(images_paths) / 1000

    for image_path in images_paths:
        clip = ImageClip(image_path)
        clip.duration = duration_per_image
        clips.append(clip)
    video = concatenate_videoclips(clips, method="compose")
    audio = AudioFileClip(audio_path)
    video.audio = audio
    video.write_videofile(output_path, fps=24)
