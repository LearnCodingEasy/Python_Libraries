
from PIL import Image

image = Image.open("./Image/Image_Png.png")

new_size_pixel = (250, 250)

resized_image = image.resize(new_size_pixel)

save_path = "./Image/Image_Resized_Pixel.png"

resized_image.save(save_path)

print(f"The image was saved in: {save_path}")

Image.open(save_path).show()

