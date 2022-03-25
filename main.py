'''
###################################
#       PYTHON AUTOCLICKER        #
#          BY Divdude77           #
###################################
'''

#############################################
# READ readme.md BEFORE RUNNING THIS SCRIPT #
#############################################

import pyautogui
import keyboard
import threading
import time

# Key which activates autoclicker
key = "v"


def clickthread():
    pyautogui.click()


print("Autoclicker Initiated!")
while True:
    if keyboard.is_pressed(key):
        while keyboard.is_pressed(key):
            time.sleep(0)                   # Delay between each click (0 -> Fastest clicking)
            x = threading.Thread(target=clickthread)
            x.start()
