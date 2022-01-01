import pyautogui as gui
from time import sleep
four_angel = 0

while True:
    if gui.locateOnScreen("four_angel.png", confidence=0.8):
        four_angel += 1
        x, y = gui.position()

        print(four_angel)
        sleep(1)



