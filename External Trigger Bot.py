import time
import pyautogui
import keyboard
import ctypes
import platform
from PIL import ImageGrab

def set_console_title(title):
    if platform.system() == "Windows":
        ctypes.windll.kernel32.SetConsoleTitleW(title)
    elif platform.system() == "Linux":
        print(f"\033]0;{title}\007", end="", flush=True)

def get_pixel_color(x, y):
    pixel = ImageGrab.grab(bbox=(x, y, x + 1, y + 1)).getpixel((0, 0))
    return pixel

def rgb_to_hex(rgb):
    return "#{:02x}{:02x}{:02x}".format(rgb[0], rgb[1], rgb[2])




new_title = "Tea Client"

set_console_title(new_title)





target_x = 959
target_y = 528


clicks_active = False

print("Press 'H' key to activate trigger bot")


try:
    while True:
        if keyboard.is_pressed('H'):
            clicks_active = not clicks_active
            if clicks_active:
                print("Automatic clicks started.")
            else:
                print("Automatic clicks stopped.")
            while keyboard.is_pressed('H'):  
                pass

        if clicks_active:
            pixel_color = get_pixel_color(target_x, target_y)
            hex_color = rgb_to_hex(pixel_color)

            
            if hex_color == "#ff0000":
                pyautogui.click(x=target_x, y=target_y)

except KeyboardInterrupt:
    print("Script terminated by user.")
