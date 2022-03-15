import pyautogui as gui
from time import sleep
import random
import webbrowser
while True:
    sleep(1)
    x, y = gui.position()
    print(x, y)

