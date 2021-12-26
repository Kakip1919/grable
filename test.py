import pyautogui
from time import sleep
while True:
    x,y = pyautogui.position()
    print(x, y)
    sleep(1)

