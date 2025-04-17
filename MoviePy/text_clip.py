

# from moviepy import VideoClip, TextClip, CompositeVideoClip, vfx
# from moviepy.Clip import Clip
# from moviepy.Effect import Effect
# import numpy as np
# from dataclasses import dataclass

# # ___________________________________

# # Add Text To Video
# font = "./Font/Omnes Bold.ttf"

# # Setting up animated text
# text_position = TextClip(
#     text="Hello, MoviePy! ",
#     font=font,
#     font_size=200,
#     color="red",
#     duration=5,
# )

# # ___________________________________

# # تحريك النص من أسفل إلى أعلى
# # 🎥 تحريك النص وفق المطلوب


# def position_func(t):
#     screen_height = 1080  # ارتفاع الفيديو
#     text_height = 200  # ارتفاع النص
#     center_y = (screen_height - text_height) // 2  # منتصف الشاشة

#     if t < 1:  # 🚀 أول ثانية: يبقى مختفيًا أسفل الشاشة
#         return ("center", screen_height)
#     elif 1 <= t < 2:  # 🚀 من الثانية 1 إلى 2: يتحرك إلى المنتصف
#         return ("center", screen_height - ((t - 1) * (screen_height - center_y)))
#     elif 2 <= t < 4:  # 🚀 من الثانية 2 إلى 4: يبقى في المنتصف
#         return ("center", center_y)
#     else:  # 🚀 من الثانية 4 إلى 5: يتحرك للأعلى حتى يختفي
#         return ("center", center_y - ((t - 4) * (center_y + text_height)))


# # ⏳ ضبط حركة النص
# animated_text = text_position.with_position(position_func)

# # 🎬 إنشاء الفيديو النهائي
# video_animated_text = CompositeVideoClip([animated_text], size=(1920, 1080))

# # Export video
# # video_animated_text.write_videofile(
# #     r"MoviePy\Video\video_scrolling_text.mp4", fps=30)
# # ___________________________________

# # نص متحرك يظهر على شكل آلة كاتبة
# # Animated text that appears as a typewriter


# def text_typing(t):
#     text = "Hello, MoviePy!"
#     # إظهار النص تدريجيًا
#     # Show text gradually
#     return text[:int(t * len(text) / 2)]

# # إنشاء قائمة من المقاطع النصية لكل لحظة زمنية
# # Create a list of text clips for each moment in time


# def make_frame(t):
#     txt_clip = TextClip(text=text_typing(t), font=font,
#                         font_size=100, color='white', size=(1920, 1080),)
#     # استخدم `get_frame(0)` للحصول على صورة ثابتة لكل لحظة
#     return txt_clip.get_frame(0)


# # make_frame إنشاء فيديو بناءً على الوظيفة
# text_clip = VideoClip(make_frame, duration=10)

# # Export video
# # text_clip.write_videofile(r"MoviePy\Video\video_typing_effect.mp4", fps=60)

# # ___________________________________
# # horizontal line extending over time


# def make_time_line(t):
#     text = TextClip(
#         text="_" * int(t * 70),
#         font=font,
#         font_size=50,
#         color='#ff7675',
#         size=(1920, 1080),
#         duration=2
#     )
#     # إرجاع صورة الإطار وليس الكائن نفسه
#     return text.get_frame(t)


# video_time_line = VideoClip(make_time_line, duration=5)
# # video_time_line.write_videofile(r"MoviePy\Video\video_timeline_effect.mp4", fps=24)

# # ___________________________________
# # ساعة رقمية تتغير مع الوقت


# def make_clock_time(t):
#     text = TextClip(
#         text=f"{int(t // 60):02}:{int(t % 60):02}",
#         font=font,
#         font_size=200,
#         color='#fdcb6e',
#         size=(1920, 1080),
#         duration=1
#     )
#     return text.get_frame(t)


# video_clock_time = VideoClip(make_clock_time, duration=15)
# # video_clock_time.write_videofile(
# #     r"MoviePy\Video\video_digital_clock.mp4", fps=60)

# # ___________________________________

# # Text fade effect
# # تأثير ظهور النص تدريجيًا
# # تعريف تأثير FadeIn المخصص


# @dataclass
# class FadeIn(Effect):
#     duration: float
#     initial_color: list = None

#     def apply(self, clip: Clip) -> Clip:
#         if self.initial_color is None:
#             self.initial_color = 0 if clip.is_mask else [0, 0, 0]
#         self.initial_color = np.array(self.initial_color)

#         def filter(get_frame, t):
#             if t >= self.duration:
#                 return get_frame(t)
#             else:
#                 fading = 1.0 * t / self.duration
#                 return fading * get_frame(t) + (1 - fading) * self.initial_color
#         return clip.transform(filter)


# # إعدادات النص
# text_fade = TextClip(
#     text="Hello, MoviePy!",
#     font=font,
#     font_size=200,
#     color="red",
#     duration=5,
#     size=(1920, 1080)
# )

# # تطبيق تأثير الظهور التدريجي باستخدام الكود المخصص
# faded_text = FadeIn(2).apply(text_fade)

# # دمج النص في فيديو
# final_clip = CompositeVideoClip([faded_text])

# # تصدير الفيديو
# # final_clip.write_videofile(
# #     r"MoviePy\Video\video_fade_text.mp4",
# #     fps=60,
# #     codec="libx264"
# # )

# # ___________________________________
# # تغيير اللون تدريجيًا


# # قائمة الألوان
# colors = ["#fdcb6e", "#ff7675", "#55efc4", "#6c5ce7", "#00cec9"]

# # إنشاء النص بمقاطع متغيرة اللون
# clips = [
#     TextClip(
#         text="Hello, MoviePy!",
#         font=font,
#         font_size=200,
#         color=colors[i],
#         size=(1920, 1080),
#         duration=1  # مدة كل كليب ثانية واحدة
#     ).with_start(i)  # كل مقطع يبدأ عند الثانية i
#     for i in range(len(colors))
# ]

# # دمج جميع المقاطع في فيديو نهائي
# final_clip_color_change = CompositeVideoClip(clips)

# # حفظ الفيديو
# final_clip_color_change.write_videofile(
#     r"MoviePy\Video\video_text_color_change.mp4", fps=60, codec="libx264")
