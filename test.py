import pyautogui as gui
from time import sleep

while True:
    x, y = gui.locateCenterOnScreen('OK.png', confidence=0.8)
    lft, t, w, h = gui.locateOnScreen("OK.png", confidence=0.8)
    print(int(w / 2), int(h / 2))
    print(x, y)
    sleep(1)




