

from PIL import Image

image = Image.open("./Image/Image_Png.png")


width, height = image.size

print(width, height)

new_size_pixel = (1200, 630)

resized_image = image.resize(new_size_pixel)

resized_image.show()

save_path = "./Image/NPM_resized.jpg"

resized_image.save(save_path)

print(f" The image was saved in: {save_path}")
