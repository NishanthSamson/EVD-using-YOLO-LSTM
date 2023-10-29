from moviepy.editor import VideoFileClip

def convert_to_mp3(input_video):

    input_file = input_video

    # Output MP3 file
    output_file = "output_audio.mp3"

    # Load the video clip
    video_clip = VideoFileClip(input_file)

    # Extract the audio from the video clip
    audio_clip = video_clip.audio

    # Write the audio to an MP3 file
    audio_clip.write_audiofile(output_file)

    # Close the clips to free up resources
    audio_clip.close()
    video_clip.close()

