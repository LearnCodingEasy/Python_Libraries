
# 1 Install Library [MoviePy]
"""
```
pip install moviepy
```
"""

# ___________________________________
# ___________________________________
# ___________________________________

# 2 Import Library [MoviePy]
"""
1 
2 VideoFileClip   | Play videos from files on the device
3 TextClip        | Fore Write Text On Video
4 
5 
6 
7 
8 
9 
10
"""
import numpy as np
from moviepy import VideoClip, VideoFileClip, TextClip, CompositeVideoClip, ImageSequenceClip, AudioFileClip
import os


# ___________________________________
# ___________________________________
# ___________________________________

# 3 Loding Video Path

# video_path = r"Video\Video.mp4"
video_path = r"F:\Python_Libraries\MoviePy\Video\Video.mp4"
video = VideoFileClip(video_path)

# التحقق من وجود الملف
if os.path.exists(video_path):
    print("The video is correct")
else:
    print("The video is incorrect.")


# ___________________________________
# ___________________________________
# ___________________________________

# Video Information

# Video duration in Seconds
duration = video.duration
print(f"Video Duration: {duration:.2f} Seconds")


# Frame Rate Per Second
fps = video.fps
print(f"Video Frame Rate: {fps} FPS")


# Video size (width x height)
size = video.size
print(f"Video Size: {size} Pixel")

# Video width and height
width, height = video.w, video.h
print(f"Video Dimensions: {width}x{height} Pixel")

# Check If The Video Has Sound
audio = video.audio
print(f"Does It Have Sound? {'Yes' if audio else 'Nos'}")

# Number Of Frames In The Video
frame_count = int(video.fps * video.duration)
print(f"Total Number Of Frames: {frame_count}")

# ___________________________________
# ___________________________________
# ___________________________________

# دالة لإنشاء صورة بلون معين عند أي لحظة زمنية


def make_frame(t):
    # لون أحمر
    return np.full((1080, 1920, 3), (255, 0, 0), dtype=np.uint8)


# إنشاء فيديو بلون أحمر لمدة 5 ثوانٍ
clip_color = VideoClip(make_frame, duration=5)
clip_color.write_videofile(r"MoviePy\Video\red_clip.mp4", fps=30)

# ___________________________________
# ___________________________________
# ___________________________________

# Cut a Part Of The Video
# From second 0 to 10
clip = video.subclipped(0, 10)
clip.write_videofile(r"MoviePy\Video\clip_0_10.mp4", codec="libx264")

# ___________________________________
# ___________________________________
# ___________________________________

# Add Text To Video
font = "./Font/Omnes Bold.ttf"
text = TextClip(
    text="Hello, MoviePy! ",
    font=font,
    font_size=100,
    color="red",
    bg_color="#FFFFFF",
    duration=5,
    stroke_color="black",
    stroke_width=2,
    text_align='left',
    horizontal_align='center',
    vertical_align='center',)
video_with_text = CompositeVideoClip([video, text])
video_with_text.write_videofile(
    r"MoviePy\Video\video_with_text.mp4", fps=30)

text_clip = TextClip(
    text="Hello, MoviePy!",
    font=font,
    font_size=300,
    color="white",
    bg_color="#6c5ce7",
    duration=5,
    stroke_color="black",
    stroke_width=1,
    text_align="center",
    horizontal_align="center",
    vertical_align="center",
    interline=5,
    transparent=True,
    margin=(10, 20),
    method="caption",
    size=(1920, 1080),
)

text_clip.write_videofile(r"MoviePy\Video\text_video.mp4", fps=60)

# ___________________________________
# ___________________________________
# ___________________________________
