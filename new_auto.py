import webbrowser
import requests
import pyautogui as gui
import random
from time import sleep

size = "Size(width=1920, height=1080)"


# ショートカットキーで削除
def close_window():
    import pyautogui

    pyautogui.keyDown('ctrl')
    pyautogui.press('w')
    pyautogui.keyUp('ctrl')
    return


# x, yは下限を返し、widthとheightは最終的な上限を返す
def pos(img):
    x, y = gui.locateCenterOnScreen(img, confidence=0.7)
    left, top, max_x, max_y = gui.locateOnScreen(img, confidence=0.7)
    x -= max_x / 2
    y -= max_y / 2
    max_x += x
    max_y += y

    return int(x), int(y+5), int(max_x), int(max_y)


def random_pos(img):
    return random.randrange(pos(img)[0], pos(img)[2]), random.randrange(pos(img)[1], pos(img)[3])


def partic():
    i = 0
    webbrowser.open("http://game.granbluefantasy.jp/#quest/assist")
    while True:

        i += 1
        if str(gui.size()) == size:
            sleep(5)
            gui.moveTo(random_pos("id_insert.png")[0], random_pos("id_insert.png")[1]
                       , random.uniform(0.8, 1.3))
            sleep(random.uniform(0.6, 1))
            gui.click()

            gui.moveTo(gui.locateCenterOnScreen('input.png'))
            gui.click()
            sleep(random.uniform(0.3, 1))

            if gui.locateOnScreen('screen.png', confidence=0.6):
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

            gui.moveTo(random_pos("assign.png")[0], random_pos("assign.png")[1]
                       , random.uniform(0.8, 1.3))
            gui.click()
            sleep(random.uniform(0.5, 1))

            if gui.locateOnScreen('Nothing_AP.png', confidence=0.9):
                gui.moveTo(random.randrange(612, 722), random.randrange(682, 703), random.uniform(0.5, 1.0))
                gui.click()
                sleep(random.uniform(0.5, 0.7))

                gui.moveTo(random.randrange(630, 719), random.randrange(625, 644), random.uniform(0.5, 1.0))
                gui.scroll(-1300)
                sleep(random.uniform(0.5, 1))
                gui.click()

                gui.moveTo(random.randrange(623, 728), random.randrange(739, 748), random.uniform(0.5, 1.0))
                sleep(random.uniform(1, 1.3))
                gui.click()

                gui.moveTo(random.randrange(496, 648), random.randrange(677, 690), random.uniform(0.5, 1.0))
                sleep(random.uniform(0.5, 1.3))
                gui.click()

            if gui.locateOnScreen('supporter.png', confidence=0.7):
                while True:
                    if gui.locateOnScreen('agnis5.png', confidence=0.9):
                        gui.moveTo(random_pos("agnis5.png")[0], random_pos("agnis5.png")[1],
                                   random.uniform(0.8, 1.3))
                        break
                    elif gui.locateOnScreen('agnis4.png', confidence=0.9):
                        gui.moveTo(random_pos("agnis4.png")[0], random_pos("agnis4.png")[1],
                                   random.uniform(0.8, 1.3))
                        break
                    elif gui.locateOnScreen('shiva.png', confidence=0.9):
                        gui.moveTo(random_pos("shiva.png")[0], random_pos("shiva.png")[1],
                                   random.uniform(0.8, 1.3))
                        break
                    else:
                        gui.scroll(-600)
            else:
                close_window()

            gui.click()
            sleep(random.uniform(0.3, 1))
            gui.moveTo(random_pos("OK.png")[0], random_pos("OK.png")[1],
                       random.uniform(0.8, 1.3))
            gui.click()

            while True:
                if gui.locateOnScreen('full.png', confidence=0.6):
                    break
                else:
                    pass
            gui.moveTo(random.randrange(348, 411), random.randrange(480, 484), random.uniform(0.8, 1.3))
            gui.click()

            if i == 50:
                break

            while True:
                if gui.locateOnScreen('result.png', confidence=0.5):
                    close_window()
                    webbrowser.open("http://game.granbluefantasy.jp/#quest/assist")
                    break
                elif gui.locateOnScreen('battle_completed.png', confidence=0.5):
                    close_window()
                    webbrowser.open("http://game.granbluefantasy.jp/#quest/assist")
                    break
                else:
                    sleep(5)


partic()
