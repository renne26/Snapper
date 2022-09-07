
import cv2

import pyautogui

#(101, 45, 102)arknights
#(90,5, 105)genshin
#(97, 0 , 150)TOF
pyautogui.PAUSE = 0.1
pyautogui.FAILSAFE = True
isclick=False
while isclick == False:
    try:
        x, y= pyautogui.locateCenterOnScreen("arknights.PNG", confidence = 0.60)
        pyautogui.moveTo(x, y, 2)
        pyautogui.click(x, y,clicks=2, interval=1, button='left')
        print("clicking")
        isclick=True

    except:
        print('not found')




















































