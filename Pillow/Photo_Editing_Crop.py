

# Pillow تعديل الصور (قص، تغيير الحجم، التدوير) باستخدام
from PIL import Image

# فتح الصورة
# image = Image.open(r"F:\Python_Libraries\Pillow\Image\/image_1_450x450.png")
image = Image.open(r"F:\Python_Libraries\Pillow\Image\/NPM.jpg")
# image = Image.open(r"F:\Python_Libraries\Pillow\Image\/NPM.jpg")

# عرض أبعاد الصورة الأصلية
width, height = image.size
print(f"أبعاد الصورة: {width}x{height}")


# # (left, top, right, bottom)
# cropped_image = image.crop((50, 50, 300, 300))
# cropped_image.show()
# # عرض الصورة
# cropped_image.show()

# ____________________________
# ____________________________
# ____________________________
# # تحديد القيم بناءً على القياسات المطلوبة
# left = max(0, 50)  # يجب أن تكون ≥ 0
# top = max(0, 50)
# right = min(300, width)   # يجب ألا تتجاوز العرض
# bottom = min(300, height)  # يجب ألا تتجاوز الارتفاع

# # التأكد من أن القيم منطقية (right يجب أن يكون > left و bottom > top)
# if right > left and bottom > top:
#     cropped_image = image.crop((left, top, right, bottom))
#     cropped_image.show()
# else:
#     print("⚠️ قيم الاقتصاص غير صحيحة، تحقق من الإدخال!")


# ____________________________
# ____________________________
# ____________________________
# # تحديد القيم بناءً على القياسات المطلوبة
# left = max(0, 150)  # يجب أن تكون ≥ 0
# top = max(0, 150)
# right = min(50, width)   # يجب ألا تتجاوز العرض
# bottom = min(50, height)  # يجب ألا تتجاوز الارتفاع

# # التأكد من أن القيم منطقية (right يجب أن يكون > left و bottom > top)
# if right > left and bottom > top:
#     cropped_image = image.crop((left, top, right, bottom))
#     cropped_image.show()
# else:
#     print("⚠️ قيم الاقتصاص غير صحيحة، تحقق من الإدخال!")


# ____________________________
# ____________________________
# ____________________________

# left = 630
# top = 100
# right = 1200
# bottom = 1200
# cropped_image = image.crop((left, top, right, bottom))
# cropped_image.show()


# ____________________________
# ____________________________
# ____________________________

def crop_with_aspect_ratio(image, aspect_ratio):
    original_width, original_height = image.size

    if original_width / original_height > aspect_ratio:
        new_width = int(original_height * aspect_ratio)
        new_height = original_height
    else:
        new_width = original_width
        new_height = int(original_width / aspect_ratio)

    left = (original_width - new_width) // 2
    top = (original_height - new_height) // 2
    right = left + new_width
    bottom = top + new_height

    return image.crop((left, top, right, bottom))


# مثال: قص الصورة بنسبة 16:9
cropped_image = crop_with_aspect_ratio(image, 2.39/1)
# cropped_image = crop_with_aspect_ratio(image, 1/1) # X
# cropped_image = crop_with_aspect_ratio(image, 4/3) # X
# cropped_image = crop_with_aspect_ratio(image, 16/9) # X
# cropped_image = crop_with_aspect_ratio(image, 21/9) # 450X192
# cropped_image = crop_with_aspect_ratio(image, 3/2) # 450X300
# cropped_image = crop_with_aspect_ratio(image, 5/4) # 450X360
# cropped_image = crop_with_aspect_ratio(image, 9/16) # 450X360
# cropped_image = crop_with_aspect_ratio(image, 9/16) # 450X360
cropped_image.show()

# ____________________________
# ____________________________
# ____________________________


# ____________________________
# ____________________________
# ____________________________

# حفظ الصورة الجديدة
save_path = r"F:\Python_Libraries\Pillow\Image\image_Crop.png"
cropped_image.save(save_path)
print(f" The image was saved in: {save_path}")
