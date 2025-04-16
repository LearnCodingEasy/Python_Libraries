
from PIL import Image

# Get image path
image_png = Image.open("./Image/Image_Png.png")
image_jpg = Image.open("./Image/Image_Jpg.jpg")
image_gif = Image.open("./Image/Image_Gif.gif")


print("📂 File Name:", image_png.filename)

print('_' * 50)

width, height = image_png.size
print("📐 Dimensions (Width x Length):", image_png.size)
print("📐 Dimensions (Width):", width)
print("📐 Dimensions (Length):", height)
print('_' * 50)

# Like RGB, RGBA, L...
print("🧬 The Situation (Mode):", image_jpg.mode)
print('_' * 50)

# JPEG, PNG, etc.
print("📷 Type:", image_png.format)
print('_' * 50)

print("🔁 Modification:", image_png.readonly)
print("🔁 Modification:", image_jpg.readonly)
print("🔁 Modification:", image_gif.readonly)
print('_' * 50)

# ('R', 'G', 'B')
print("🧪 Channels:", image_jpg.getbands())
print("🔢 Number of channels:", len(image_jpg.getbands()))
print('_' * 50)

# Additional Information If Available
print("🧾 Additional information (info):", image_jpg.info)
