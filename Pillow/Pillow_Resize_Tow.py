
from PIL import Image

image = Image.open("./Image/Image_Png.png")


width, height = image.size

new_img = image.resize((width // 2, height // 2))

save_path = "./Image/Image_Resized_Half.png"

new_img.save(save_path)

print(f"The image was saved in: {save_path}")

Image.open(save_path).show()
