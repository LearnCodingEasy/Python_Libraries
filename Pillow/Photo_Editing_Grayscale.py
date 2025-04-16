

# Pillow تعديل الألوان والفلاتر (تدرجات الرمادي، تغيير الحجم، التدوير) باستخدام
from PIL import Image

# فتح الصورة
# image = Image.open(r"F:\Python_Libraries\Pillow\Image\/image_1_450x450.png")
image = Image.open(r"F:\Python_Libraries\Pillow\Image\/NPM.jpg")
# image = Image.open(r"F:\Python_Libraries\Pillow\Image\/NPM.jpg")


# ____________________________
# ____________________________
# ____________________________

grayscale_image = image.convert("L")
grayscale_image.show()


# ____________________________
# ____________________________
# ____________________________


# ____________________________
# ____________________________
# ____________________________

# حفظ الصورة الجديدة
save_path = r"F:\Python_Libraries\Pillow\Image\grayscale_image.png"
grayscale_image.save(save_path)
print(f" The image was saved in: {save_path}")
