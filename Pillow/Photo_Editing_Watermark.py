

# Pillow إضافة علامة مائية شفافة باستخدام
from PIL import Image
from PIL import ImageDraw, ImageFont

# فتح الصورة
# image = Image.open(r"F:\Python_Libraries\Pillow\Image\/image_1_450x450.png")
# image = Image.open(r"F:\Python_Libraries\Pillow\Image\/image_1_450x450.webp")
image = Image.open(r"F:\Python_Libraries\Pillow\Image\/NPM.jpg")
# image = Image.open(r"F:\Python_Libraries\Pillow\Image\/Video.png")


# ____________________________
# ____________________________
# ____________________________


watermark = Image.open(
    r"F:\Python_Libraries\Pillow\Image\/image_1_450x450.png").convert("RGBA")

# ضبط حجم العلامة المائية
watermark = watermark.resize((75, 75))

# دمج العلامة المائية مع الصورة الأصلية
image.paste(watermark, (50, 50), watermark)

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
