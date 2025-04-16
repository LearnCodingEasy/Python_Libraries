

# Pillow الكتابة على الصور باستخدام
from PIL import Image
from PIL import ImageDraw, ImageFont

# فتح الصورة
# image = Image.open(r"F:\Python_Libraries\Pillow\Image\/image_1_450x450.png")
image = Image.open(r"F:\Python_Libraries\Pillow\Image\/image_1_450x450.webp")
# image = Image.open(r"F:\Python_Libraries\Pillow\Image\/NPM.jpg")
# image = Image.open(r"F:\Python_Libraries\Pillow\Image\/Video.jpg")


# ____________________________
# ____________________________
# ____________________________

# إنشاء كائن للرسم
draw = ImageDraw.Draw(image)

# تحميل خط (يجب أن يكون لديك ملف خط TTF)

font = ImageFont.truetype("F:\Python_Libraries\Pillow\Font\Omnes_Bold.ttf", 60)

# إضافة النص
draw.text((50, 50), "Hello, Pillow!", fill="white", font=font)

# عرض الصورة
image.show()


# ____________________________
# ____________________________
# ____________________________


# ____________________________
# ____________________________
# ____________________________

# حفظ الصورة الجديدة
save_path = r"F:\Python_Libraries\Pillow\Image\image_draw.png"
image.save(save_path)
print(f" The image was saved in: {save_path}")
