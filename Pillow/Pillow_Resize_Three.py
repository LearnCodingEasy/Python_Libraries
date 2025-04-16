
from PIL import Image

image = Image.open("./Image/Image_Png.png")

new_img = image.resize((250, 250), Image.Resampling.LANCZOS)

save_path = "./Image/Image_Resized_Quality.png"

new_img.save(save_path)

print(f"The image was saved in: {save_path}")

Image.open(save_path).show()
