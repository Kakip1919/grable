import webbrowser
import requests
import pyautogui as gui
import random
from time import sleep
import os
size = "Size(width=1920, height=1080)"


def partic():
    i = 0

    while True:
        i += 1
        webbrowser.open("http://game.granbluefantasy.jp/#quest/assist")
        if str(gui.size()) == size:
            sleep(5)
            gui.moveTo(random.randrange(674, 795), random.randrange(276, 310), random.uniform(0.8, 1.3))
            sleep(random.uniform(0.6, 1))
            gui.click()
            gui.moveTo(random.randrange(398, 542), random.randrange(551, 565), random.uniform(0.8, 1.3))
            gui.click()
            sleep(random.uniform(0.3, 1))

            if gui.locateOnScreen('screen.png', confidence=0.9):
                gui.moveTo(random.randrange(495, 608), random.randrange(635, 638), random.uniform(0.8, 1.3))
                gui.click()
                gui.moveTo(random.randrange(398, 542), random.randrange(551, 565), random.uniform(0.8, 1.3))
                gui.click()
                sleep(random.uniform(0.3, 1))
                res = requests.get('http://127.0.0.1:8888/')
                res = res.json()["war_code"]
                gui.write(res)

            else:
                res = requests.get('http://127.0.0.1:8888/')
                res = res.json()["war_code"]
                gui.write(res)

            gui.moveTo(random.randrange(609, 724), random.randrange(541, 560), random.uniform(0.8, 1.3))
            gui.click()
            sleep(random.uniform(0.5, 1))
            print(gui.locateOnScreen('agnis5.png', confidence=0.9))
            while True:
                if gui.locateOnScreen('agnis5.png', confidence=0.9):
                    position = gui.locateOnScreen('agnis5.png', confidence=0.9)
                    break
                elif gui.locateOnScreen('agnis4.png', confidence=0.9):
                    position = gui.locateOnScreen('agnis4.png', confidence=0.9)
                    break
                elif gui.locateOnScreen('shiva.png', confidence=0.9):
                    position = gui.locateOnScreen('shiva.png', confidence=0.9)
                    break
                else:
                    gui.scroll(-600)

            gui.click(position)
            gui.moveTo(random.randrange(591, 705), random.randrange(740, 750), random.uniform(0.8, 1.3))
            sleep(random.uniform(0.3, 1))
            gui.click()
            sleep(3.5)
            gui.moveTo(random.randrange(348, 411), random.randrange(480, 484), random.uniform(0.8, 1.3))
            gui.click()
            sleep(100)
            if i == 50:
                break


partic()
