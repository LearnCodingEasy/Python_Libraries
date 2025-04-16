

# Pillow تعديل الألوان والفلاتر (تدرجات الرمادي، تغيير ألوان الصورة، التمويه ) باستخدام
from PIL import Image
from PIL import ImageFilter

# فتح الصورة
# image = Image.open(r"F:\Python_Libraries\Pillow\Image\/image_1_450x450.png")
image = Image.open(r"F:\Python_Libraries\Pillow\Image\/image_1_450x450.webp")
# image = Image.open(r"F:\Python_Libraries\Pillow\Image\/NPM.jpg")
# image = Image.open(r"F:\Python_Libraries\Pillow\Image\/Video.jpg")


# ____________________________
# ____________________________
# ____________________________

blurred_image = image.filter(ImageFilter.GaussianBlur(5))
blurred_image.show()



# ____________________________
# ____________________________
# ____________________________


# ____________________________
# ____________________________
# ____________________________

# حفظ الصورة الجديدة
save_path = r"F:\Python_Libraries\Pillow\Image\blurred_image.png"
blurred_image.save(save_path)
print(f" The image was saved in: {save_path}")
