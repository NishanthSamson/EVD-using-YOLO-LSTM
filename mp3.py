from moviepy.editor import VideoFileClip


def convert_to_mp3(input_video):
    input_file = input_video
    output_file = "output_audio.mp3"

    video_clip = VideoFileClip(input_file)
    audio_clip = video_clip.audio

    audio_clip.write_audiofile(output_file)

    audio_clip.close()
    video_clip.close()
