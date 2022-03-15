import webbrowser
import pyautogui as gui
import random
from time import sleep

size = "Size(width=1920, height=1080)"


def close_window():
    import pyautogui
    pyautogui.keyDown('ctrl')
    pyautogui.press('w')
    pyautogui.keyUp('ctrl')
    return


def partner():
    # 救援ボタン
    gui.moveTo(random.randrange(360, 513), random.randrange(845, 862), random.uniform(0.6, 1))
    gui.click()
    # 救援するボタン
    gui.moveTo(random.randrange(605, 756), random.randrange(710, 729), random.uniform(0.6, 1))
    gui.click()
    # OKボタン
    gui.moveTo(random.randrange(498, 678), random.randrange(627, 691), random.uniform(0.6, 1))
    gui.click()


def single_play(values, summon_stone):
    stone_genre = values[0]
    element = values[1]
    i = 0
    iters = 1
    count = 0
    while True:
        webbrowser.open(values[3])
        i += 1
        while True:
            sleep(random.uniform(1, 1.5))
            if gui.locateOnScreen(summon_stone[stone_genre][element][str(iters)], confidence=0.9):
                position = gui.locateOnScreen(summon_stone[stone_genre][element][str(iters)],
                                              confidence=0.9)
                sleep(random.uniform(0.5, 0.7))
                gui.click(position)
                sleep(random.uniform(0.5, 1))
                break
            else:
                count += 1
                gui.scroll(-600)
                sleep(random.uniform(0.3, 0.5))
                if iters == len(summon_stone[stone_genre][element]):
                    gui.moveTo(random.randrange(379, 679), random.randrange(740,771), random.uniform(0.5, 1.0))
                    gui.click()
                    sleep(random.uniform(0.5, 0.7))
                    break
                if count >= 5:
                    gui.scroll(3000)
                    iters += 1
                    count = 0

        gui.moveTo(random.randrange(591, 705), random.randrange(740, 750), random.uniform(0.8, 1.3))
        gui.click()
        sleep(random.uniform(0.7, 1))

        if gui.locateOnScreen("single_battle/not_api.png", confidence=0.7):
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
            sleep(random.uniform(0.5, 0.8))
            gui.click()

        while True:
            sleep(random.uniform(0.5, 1))
            if gui.locateOnScreen('single_battle/full.png', confidence=0.7):
                gui.moveTo(random.randrange(348, 411), random.randrange(480, 484), random.uniform(0.8, 1.3))
                gui.click()
                # partner()
                break
            else:
                pass

        if i == int(values[2]):
            break

        while True:
            sleep(random.uniform(0.5, 1))
            if gui.locateOnScreen('single_battle/OK.png', confidence=0.7):
                sleep(random.uniform(0.5, 1))
                close_window()
                break
            else:
                print("待機中")
                sleep(2)
