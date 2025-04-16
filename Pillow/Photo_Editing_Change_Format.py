

# Pillow إضافة علامة مائية شفافة باستخدام
from PIL import Image
from PIL import ImageDraw, ImageFont

# فتح الصورة
# image = Image.open(r"F:\Python_Libraries\Pillow\Image\/image_1_450x450.png")
# image = Image.open(r"F:\Python_Libraries\Pillow\Image\/image_1_450x450.webp")
# image = Image.open(r"F:\Python_Libraries\Pillow\Image\/NPM.jpg")
image = Image.open(r"F:\Python_Libraries\Pillow\Image\/Video.png")
# image = Image.open(r"F:\Python_Libraries\Pillow\Image\/Video.jpg")


# ____________________________
# ____________________________
# ____________________________

image = image.convert("RGB")

# ____________________________
# ____________________________
# ____________________________


# ____________________________
# ____________________________
# ____________________________

# حفظ الصورة الجديدة
save_path = r"F:\Python_Libraries\Pillow\Image\Image_Change_Format.png"
# PNG حفظ الصورة كملف
# image.save(save_path, format="PNG")
image.save(save_path, format="JPEG")
# image.save(save_path, format="JPG")
print(f" The image was saved in: {save_path}")


# ____________________________
# ____________________________
# ____________________________

# عرض الصورة
image.show()
