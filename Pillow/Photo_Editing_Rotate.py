

# Pillow تعديل الصور (قص، تغيير الحجم، التدوير) باستخدام
from PIL import Image

# فتح الصورة
image = Image.open(r"F:\Python_Libraries\Pillow\Image\/Video.png")

rotated_image = image.rotate(45)  # تدوير 45 درجة
# عرض الصورة
rotated_image.show()


# حفظ الصورة الجديدة
save_path = r"F:\Python_Libraries\Pillow\Image\Video_Rotate.png"
rotated_image.save(save_path)

print(f" The image was saved in: {save_path}")
