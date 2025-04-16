

# Pillow تعديل الألوان والفلاتر (تدرجات الرمادي، تغيير الحجم، التدوير) باستخدام
from PIL import Image
from PIL import ImageEnhance

# فتح الصورة
# image = Image.open(r"F:\Python_Libraries\Pillow\Image\/image_1_450x450.png")
image = Image.open(r"F:\Python_Libraries\Pillow\Image\/image_1_450x450.webp")
# image = Image.open(r"F:\Python_Libraries\Pillow\Image\/NPM.jpg")
# image = Image.open(r"F:\Python_Libraries\Pillow\Image\/Video.jpg")


# ____________________________
# ____________________________
# ____________________________

enhancer = ImageEnhance.Color(image)
color_enhanced = enhancer.enhance(2)  # 2 = مضاعفة التشبع
color_enhanced.show()


# ____________________________
# ____________________________
# ____________________________


# ____________________________
# ____________________________
# ____________________________

# حفظ الصورة الجديدة
save_path = r"F:\Python_Libraries\Pillow\Image\color_enhanced.png"
color_enhanced.save(save_path)
print(f" The image was saved in: {save_path}")
