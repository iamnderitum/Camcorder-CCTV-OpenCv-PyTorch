import pandas as pd
import numpy as np
import cv2
import matplotlib.pyplot as plt

from glob import glob
import subprocess

# INITIALIZE VARIABLES
image_file = "../resources/videos/personal_video.mp4"
WINDOW_HEIGHT = 600
WINDOW_WIDTH = 800


def convert_video():
    #subprocess.run(['ffmpeg', "-i", image_file, "-qscale", "0", "personal_video.mov"])

    subprocess.run(['ffmpeg',
                "-i",
                image_file,
                "-qscale",
                "0",
                "personal_video.mov",
                "-loglevel",
                "quiet"
                ]
            )

video_cap = cv2.VideoCapture(image_file)
def video_data():
    frame_counts = video_cap.get(cv2.CAP_PROP_FRAME_COUNT)
    height = video_cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    width = video_cap.get(cv2.CAP_PROP_FRAME_WIDTH)

    fps = int(video_cap.get(cv2.CAP_PROP_FPS))
    video_length_seconds = frame_counts / fps
    print(f"\nFrame Count: {frame_counts} " )
    print(f"\nHeight: {height} " )
    print(f"\nWidth: {width} " )
    print(f"\nFrame Per Seconds: {fps} " )
    print(f"\nVideo Length: {video_length_seconds:0.2f} Seconds " )

    #Pulling Image from Video
    ret, img = video_cap.read()
    print(f"\nReturned {ret} and image of shape {img.shape}")

video_data()

def display_video_frames(video_file):
    #video_file = "personal_video.mov"
    video_cap = cv2.VideoCapture(video_file)

    total_frames = int(video_cap.get(cv2.CAP_PROP_FRAME_COUNT))

    step = total_frames // 25

    fig, axs = plt.subplots(5, 5, figsize=(30,20))
    axs = axs.flatten()

    frame_counter = 0

    for i in range(25):
        video_cap.set(cv2.CAP_PROP_POS_FRAMES, frame_counter)

        ret, img = video_cap.read()
        if not ret:
            break

        # Display the frame
        axs[i].imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        axs[i].set_title(f"Frame: {frame_counter}")
        axs[i].axis("off")
        frame_counter += step

    plt.tight_layout()
    plt.show()

    img_idx = 0
    for frame in range(total_frames):
        ret, img = video_cap.read()
        if ret == False:
            break
        if frame % 10 == 0:
            axs[img_idx].imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
            axs[img_idx].set_title(f"Frame: {frame}")
            axs[img_idx].axis("off")
            img_idx += 1

    plt.tight_layout()
    plt.show()
    ch = cv2.waitKey(1)
    while True:
        if ch & 0xFF == ord("q"):
            break

    video_cap.release()
    cv2.destroyAllWindows()

cv2.destroyAllWindows()
display_video_frames("personal_video.mov")


"""
    img_idx = 0
    for frame in range(n_frames):
        ret, img = video_cap.read()
        if ret == False:
            break
        if frame % 10 == 0:
            axs[img_idx].imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
            axs[img_idx].set_title(f"Frame: {frame}")
            axs[img_idx].axis("off")
            img_idx += 1
"""

    

def play_video():
    # Create a named window with the desired size
    cv2.namedWindow("Personal Video", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Personal Video", WINDOW_WIDTH, WINDOW_HEIGHT)

    if not video_cap.isOpened():
        print("Error could not open video file")
        exit()

    while True:
        ret, frame = video_cap.read()
        if not ret:
            break

        # RESIZE the frame to fit the viewing Window
        frame_resized = cv2.resize(frame, (WINDOW_WIDTH, WINDOW_HEIGHT))
        cv2.imshow("Personal Video", frame_resized)
        if cv2.waitKey(20) & 0xFF == ord("q"):
            break



    video_cap.release()
    cv2.destroyAllWindows()

#play_video()

