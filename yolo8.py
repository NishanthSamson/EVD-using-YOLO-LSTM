from ultralytics import YOLO
from moviepy.editor import VideoFileClip
import os
import shutil


model = YOLO('models/best.pt')


def convert_to_mp4():
    input_avi_file = "static/predict/test.avi"
    output_mp4_file = "static/predict/output.mp4"

    video = VideoFileClip(input_avi_file)

    video.write_videofile(output_mp4_file, codec='libx264')
    video.close()


def predict(src):

    directory = "static/predict"
    if os.path.exists(directory) and os.path.isdir(directory):
        shutil.rmtree(directory)

    model.predict(src, show=True, save=True, project="static")
    # convert_to_mp4()
