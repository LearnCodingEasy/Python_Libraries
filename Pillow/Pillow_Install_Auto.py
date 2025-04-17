# 1 Libraries
# 🖥️ لفتح التطبيقات أو تنفيذ أوامر النظام
import subprocess

# ⌨️ لمحاكاة الكتابة والنقر وإجراءات لوحة المفاتيح والفأرة
import pyautogui

# 📋 للتعامل مع النسخ واللصق النصوص
import pyperclip

# ⏳ لإضافة التأخيرات الزمنية أثناء تنفيذ الأوامر
import time

# 🎨 لتحسين عرض النصوص في واجهة الكونسول باستخدام التنسيقات
from rich.console import Console

# 📂 التعامل مع الملفات والمجلدات
import os

# ________________________________________________________
# ________________________________________________________
# ________________________________________________________
# ________________________________________________________
# ________________________________________________________
# 2 Configuration
# 1️⃣ subprocess
# 🔍 Visual Studio Code البحث عن مسار
result = subprocess.run(["where", "code"], capture_output=True, text=True)
# ✅ التحقق من نجاح العثور على المسار
if result.returncode == 0:
    # عرض المسار إذا تم العثور على البرنامج
    print("✅ VS Code found:", result.stdout.strip())
else:
    # رسالة خطأ إذا لم يتم العثور على البرنامج
    print("❌ VS Code not found. Make sure it is installed.")

# 🚀 في نافذة جديدة Visual Studio Code فتح
subprocess.Popen(
    [
        # المسار المباشر لتشغيل البرنامج
        "C:\\Users\\learn\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe",
        # فتح نافذة جديدة
        "--new-window",
        # فتح المجلد الحالي
        ".",
    ]
)

# 2️⃣ Console
console = Console()

# ⚙️ التحكم في تفعيل الكتابة التلقائية
enable_auto_write = True

# 📄 "File.py" النصوص التي سيتم كتابتها داخل الملف
file_name = "Pillow_File.py"

# 📄 سرعة خط البحث في الصفحة
speed_search_line = 0.1

# 📄 وقت الانتظار إظهار الكود
time_waiting_show_code = 2

time_waiting_to_start = 1
time_waiting_v = 0.1
time_waiting_s = 0.1
time_waiting_enter = 0.1
time_waiting_search_line = 0.1
time_waiting_search_line_delay = 0.1
time_waiting_search_line_typing = 0.1
time_waiting_search_line_collapse = 0.1
time_waiting_toggle_terminal = 1

print("✅ Visual Studio Code is opened successfully!")

# ________________________________________________________
# ________________________________________________________
# ________________________________________________________
# ________________________________________________________
# ________________________________________________________

# 3 Function
# 🖊️ Automation دالة لكتابة النصوص مع محاكاة الكتابة الطبيعية


def write_like_typing_on_keypord(file_path, text, delay=0.0):
    """
    تكتب النص داخل الملف وتحاكي الكتابة الطبيعية على لوحة المفاتيح.
    :param file_path: اسم الملف الذي سيتم الكتابة فيه
    :param text: النص المراد كتابته
    :param delay: التأخير بين الحروف لمحاكاة الكتابة الطبيعية
    """
    if enable_auto_write:
        # فتح الملف في وضع الإضافة
        with open(file_path, "a") as file:
            for char in text:
                # ⌨️ محاكاة الكتابة الطبيعية
                pyautogui.typewrite(char)
                # 📝 كتابة النص داخل الملف
                file.write(char)
                # التأكد من حفظ النص مباشرة
                file.flush()
                # ⏳ التأخير بين الحروف
                time.sleep(delay)
            # 📝 الانتقال إلى سطر جديد بعد كتابة النص
            # pyautogui.write("\n")
        print(f"✅ Text written: {text}")
    else:
        print("❌ Auto write is disabled.")

# Automation دالة لتبسيط الأوامر مع محاكاة الكتابة الطبيعية


def automate_action(action, *args, delay=1, typing_delay=0.01):
    """
    يقوم بتنفيذ الأوامر تلقائيًا مع إضافة تأخير اختياري.
    :param action: نوع الإجراء (hotkey, typewrite, press, print)
    :param args: المعاملات المطلوبة للإجراء
    :param delay: تأخير قبل التنفيذ (افتراضي 1 ثانية)
    :param typing_delay: تأخير بين الأحرف عند الكتابة لمحاكاة الكتابة الطبيعية (افتراضي 0.05 ثانية)
    """
    time.sleep(delay)
    if action == "hotkey":
        pyautogui.hotkey(*args)
    elif action == "typewrite":
        # كتابة كل حرف على حدة مع تأخير
        for char in args[0]:
            pyautogui.typewrite(char)
            time.sleep(typing_delay)
    elif action == "press":
        pyautogui.press(*args)
    elif action == "print":
        console.print(*args)

# ________________________________________________________
# ________________________________________________________
# ________________________________________________________
# ________________________________________________________
# ________________________________________________________


# 4 Code 1
# ⏳ انتظار مدة معينة (10 ثوانٍ)
time.sleep(15)
automate_action("hotkey", "ctrl", "j",  delay=time_waiting_v)
time.sleep(2)
# ⏳ انتظار مدة معينة ( ثوانٍ)
time.sleep(time_waiting_show_code)
time.sleep(time_waiting_to_start)
pyperclip.copy("""pip install pillow""")
automate_action("hotkey", "ctrl", "v",  delay=time_waiting_v)


print("✅ Terminal Write Libraries Done")

time.sleep(2)

automate_action("press", "enter", delay=time_waiting_v)

print("✅ Install Libraries Done")

time.sleep(7)
automate_action("hotkey", "ctrl", "j",  delay=time_waiting_v)
# ________________________________________________________
# ________________________________________________________
# ________________________________________________________
# ________________________________________________________
# ________________________________________________________

time.sleep(3)
pyperclip.copy("""# 🖼️ Import the Pillow image processing library""")
# 💻 ShortCut فتح واجهة لصق النص
automate_action("hotkey", "ctrl", "v",  delay=time_waiting_v)
automate_action("hotkey", "ctrl", "s",  delay=time_waiting_s)
# ⏳ انتظار مدة معينة ( ثوانٍ)
time.sleep(time_waiting_show_code)
time.sleep(time_waiting_to_start)
ExampleOne = ["import PIL \n",]
# 📝 كتابة النصوص داخل الملف
for text in ExampleOne:
    # 📝 الانتقال إلى سطر جديد بعد كتابة النص
    # pyautogui.write("\n")
    write_like_typing_on_keypord(file_name, text, delay=0.0)
    # ⏳ تأخير قبل كتابة النص التالي
    time.sleep(1)
# 💻 ShortCut فتح واجهة لصق النص
automate_action("hotkey", "ctrl", "s", delay=time_waiting_s)
print("✅ Import Libraries Done")

# ________________________________________________________
# ________________________________________________________
# ________________________________________________________
# ________________________________________________________
# ________________________________________________________

# 5 Code 2 Connection
# ⏳ انتظار مدة معينة ( ثوانٍ)
time.sleep(time_waiting_show_code)
time.sleep(time_waiting_to_start)
pyperclip.copy("""\n# 🔍 Print the current version of the Pillow library""")
# 💻 ShortCut فتح واجهة لصق النص
automate_action("hotkey", "ctrl", "v",  delay=time_waiting_v)
# automate_action("hotkey", "ctrl", "s",  delay=time_waiting_s)

# ⏳ انتظار مدة معينة ( ثوانٍ)
time.sleep(time_waiting_show_code)
time.sleep(time_waiting_to_start)
ExampleTow = ['print(PIL.__version__)  \n',
              ]
# 📝 كتابة النصوص داخل الملف
for text in ExampleTow:
    # 📝 الانتقال إلى سطر جديد بعد كتابة النص
    pyautogui.write("\n")
    write_like_typing_on_keypord(file_name, text, delay=0.0)
    # ⏳ تأخير قبل كتابة النص التالي
    time.sleep(1)
# 💻 ShortCut فتح واجهة لصق النص
automate_action("hotkey", "ctrl", "s", delay=time_waiting_s)
print("✅ version Write Libraries Done")

# ________________________________________________________
# ________________________________________________________
# ________________________________________________________
# ________________________________________________________
# ________________________________________________________

time.sleep(3)
automate_action("hotkey", "ctrl", "shift", "`", delay=time_waiting_v)
time.sleep(3)

pyperclip.copy("""python Pillow_File.py""")
automate_action("hotkey", "ctrl", "v",  delay=time_waiting_v)
print("✅ Terminal Write python Pillow_File.py Done")
time.sleep(2)

automate_action("press", "enter", delay=time_waiting_v)
print("✅ Terminal Run File Done")
time.sleep(2)
