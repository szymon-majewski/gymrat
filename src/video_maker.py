from moviepy.editor import ImageClip, AudioFileClip, concatenate_videoclips


def generate_video(images_paths, audio_path, output_path, transition_duration=1):
    audio = AudioFileClip(audio_path)
    duration_per_image = audio.duration / len(images_paths)

    video_clips = []
    for idx, image_path in enumerate(images_paths):
        clip = ImageClip(image_path).set_duration(duration_per_image + transition_duration)

        if idx != 0:
            clip = clip.crossfadein(transition_duration)

        video_clips.append(clip)

    final_video = concatenate_videoclips(video_clips, method="compose", padding=-transition_duration)
    final_video = final_video.set_audio(audio)
    final_video.write_videofile(output_path, fps=24)
