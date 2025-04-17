
# # 1 Import Library [MoviePy]

# """

# """
# from moviepy import VideoClip
# import numpy as np
# import matplotlib.colors as mcolors
# import cv2


# # ___________________________________
# # Function To creates a video frame with a specific color
# def make_video_color(t):
#     # color
#     return np.full((1080, 1920, 3), (162, 155, 254), dtype=np.uint8)


# # Create a 5-second  video With Color
# clip_color = VideoClip(make_video_color, duration=5)
# clip_color.write_videofile(r"MoviePy\Video\video_color.mp4", fps=30)

# # ___________________________________

# # 🎨 Required colors in gradient
# # Starting color
# first_color = "#6c5ce7"
# # Finish color
# second_color = "#a29bfe"

# # Convert HEX colors to RGB (value between 0 and 1)
# # Convert to values ​​between 0 and 255
# first_rgb = np.array(mcolors.to_rgb(first_color)) * \
#     255
# second_rgb = np.array(mcolors.to_rgb(second_color)) * 255


# def make_video_gradient(t):
#     # Create a smooth gradient between two colors
#     # 1920 نقطة تمثل التدرج
#     gradient = np.linspace(0, 1, 1920)
#     # Repeat the gradient vertically
#     gradient = np.tile(gradient, (1080, 1))

#     # Create gradient for each channel (R, G, B)
#     red_channel = (1 - gradient) * first_rgb[0] + gradient * second_rgb[0]
#     green_channel = (1 - gradient) * first_rgb[1] + gradient * second_rgb[1]
#     blue_channel = (1 - gradient) * first_rgb[2] + gradient * second_rgb[2]

#     # Merge channels into one image
#     return np.stack([red_channel, green_channel, blue_channel], axis=-1).astype(np.uint8)


# # Create a video
# clip_gradient = VideoClip(make_video_gradient, duration=5)
# clip_gradient.write_videofile(r"MoviePy\Video\video_gradient.mp4", fps=60)

# # ___________________________________

# # Function to create a frame with a moving square


# def make_video_moving_square(t):
#     # black background
#     frame = np.zeros((1080, 1920, 3), dtype=np.uint8)
#     # Move the square over time
#     x_position = int(200 + t * 300)
#     # color square
#     cv2.rectangle(frame, (x_position, 400), (x_position +
#                   100, 500), (214, 48, 49), -1)
#     return frame


# # Create a video
# clip_moving_square = VideoClip(make_video_moving_square, duration=5)
# clip_moving_square.write_videofile(
#     r"MoviePy\Video\video_moving_square.mp4", fps=90)

# # ___________________________________

# # Function to create a wave effect


# def make_wave_effect(t):
#     # black background
#     frame = np.zeros((1080, 1920, 3), dtype=np.uint8)
#     for i in range(0, 1920, 50):
#         # wave equation
#         y_position = int(540 + 100 * np.sin(i * 0.01 + t * 2))
#         # Draw points
#         frame[y_position-5:y_position+5, i-5:i+5] = (0, 255, 255)
#     return frame


# clip_wave_effect = VideoClip(make_wave_effect, duration=5)
# clip_wave_effect.write_videofile(
#     r"MoviePy\Video\video_wave_effect.mp4", fps=120)

# # ___________________________________

# # Create a video with a flashing effect


# def make_flashing_light(t):
#     # قيمة بين 0 و 255
#     intensity = int((np.sin(t * 5) + 1) * 127)
#     return np.full((1080, 1920, 3), (intensity, intensity, intensity), dtype=np.uint8)


# clip_flashing_light = VideoClip(make_flashing_light, duration=5)
# clip_flashing_light.write_videofile(
#     r"MoviePy\Video\video_flashing_light.mp4", fps=150)


# # ___________________________________
