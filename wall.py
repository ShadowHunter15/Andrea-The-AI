from datetime import datetime
import random
import time
import ctypes
import os
from PIL import Image, ImageDraw, ImageFont
import multiprocessing
def clock():
    time_font = ImageFont.truetype(r"C:\Users\osdrw\Desktop\Programming\AndreaTheAI\BOD_BLAR.ttf", 125)
    date_font = ImageFont.truetype(r"C:\Users\osdrw\Desktop\Programming\AndreaTheAI\BOD_BLAR.ttf", 50)
    curr = datetime.now().strftime("%H:%M:%S")
    while True:   
        image = Image.open(r"C:\Users\osdrw\Desktop\Programming\AndreaTheAI\img.jpg")
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S") 
        date = datetime.today().strftime('%Y-%m-%d')
        if int(current_time[0:2]) > 12:
            current_time = str(int(current_time[0:2]) -12) + current_time[2:]
        image_editable = ImageDraw.Draw(image)
        image_editable.text((275,200), current_time, (237, 230, 211), font=time_font)
        image_editable.text((365,400), date, (237, 230, 211), font=date_font)
        image.save("1.jpg")
        ctypes.windll.user32.SystemParametersInfoW(20, 0, "C:/Users/osdrw/Desktop/Programming/AndreaTheAI/1.jpg" , 0)
        time.sleep(0.5)
def random_wallpaper():
    choice = random.choice(os.listdir(r"C:\Users\osdrw\Desktop\Programming\Wallpapers\Spotlight"))
    ctypes.windll.user32.SystemParametersInfoW(20, 0, r"C:\Users\osdrw\Desktop\Programming\Wallpapers\Spotlight\{}".format(choice), 0)