import webbrowser
import pyautogui as gui
import random
from time import sleep

size = "Size(width=1920, height=1080)"

quest = "http://game.granbluefantasy.jp/#quest/supporter/784431/3"

summon_stone = {"god": {"fire": {"2": "summon_stone/fire/god/agnis4.png",
                                 "1": "summon_stone/fire/god/agnis5.png"},
                        "water": {"2": "summon_stone/water/god/varuna4.png",
                                  "1": "summon_stone/water/god/varuna5.png"},
                        "sand": {"2": "summon_stone/sand/god/titan4.png",
                                 "1": "summon_stone/sand/god/titan5.png"},
                        "wind": {"2": "summon_stone/wind/god/zep4.png",
                                 "1": "summon_stone/wind/god/zep5.png"},
                        "light": {"2": "summon_stone/light/god/zeus4.png",
                                  "1": "summon_stone/light/god/zeus5.png"},
                        "dark": {"2": "summon_stone/dark/god/hades4.png",
                                 "1": "summon_stone/dark/god/hades5.png"}},

                "magna": {"fire": {"2": "summon_stone/fire/magna/koro4.png",
                                   "1": "summon_stone/fire/magna/koro5.png"},
                          "water": {"2": "summon_stone/water/magna/riva4.png",
                                    "1": "summon_stone/water/magna/riva5.png"},
                          "sand": {"2": "summon_stone/sand/magna/yugu4.png",
                                   "1": "summon_stone/sand/magna/yugu5.png"},
                          "wind": {"2": "summon_stone/wind/magna/tiamat4.png",
                                   "1": "summon_stone/wind/magna/tiamat5.png"},
                          "light": {"3": "summon_stone/light/magna/syuva3.png",
                                    "2": "summon_stone/light/magna/syuva4.png",
                                    "1": "summon_stone/light/magna/syuva5.png"},
                          "dark": {"2": "summon_stone/dark/magna/serest4.png",
                                   "1": "summon_stone/dark/magna/serest5.png"}},

                "provi": {"fire": {"2": "summon_stone/fire/provi/shiva4.png",
                                   "1": "summon_stone/fire/provi/shiva5.png"},
                          "water": {"europe4": "summon_stone/water/provi/europe4.png",
                                    "europe5": "summon_stone/water/provi/europe5.png"},
                          "sand": {"gobro4": "summon_stone/sand/provi/gobro4.png",
                                   "gobro5": "summon_stone/sand/provi/gobro5.png"},
                          "wind": {"grim4": "summon_stone/wind/provi/grim4.png",
                                   "grim5": "summon_stone/wind/provi/grim5.png"},
                          "light": {"rusi4": "summon_stone/light/provi/rusi4.png",
                                    "rusi5": "summon_stone/light/provi/rusi5.png"},
                          "dark": {"baha3": "summon_stone/dark/provi/baha3.png",
                                   "baha4": "summon_stone/dark/provi/baha4.png",
                                   "baha5": "summon_stone/dark/provi/baha5.png"}}}
stone_genre = input()
element = input()


def stone_select(stone):
    i = 0
    stone_array = []

    while True:
        i += 1
        stone_array.append(stone[stone_genre][element][str(i)])

        if i >= len(stone[stone_genre][element]):
            return stone_array


def close_window():
    import pyautogui

    pyautogui.keyDown('ctrl')
    pyautogui.press('w')
    pyautogui.keyUp('ctrl')
    return


def partic():
    i = 0
    webbrowser.open(quest)
    iters = 0
    count = 0
    while True:

        i += 1
        if str(gui.size()) == size:

            while True:
                sleep(random.uniform(1, 1.5))
                if gui.locateOnScreen(stone_select(summon_stone)[iters], confidence=0.9):
                    position = gui.locateOnScreen(stone_select(summon_stone)[iters], confidence=0.9)
                    break
                else:
                    count += 1
                    gui.scroll(-600)
                    sleep(random.uniform(0.3, 1))
                    if count >= 5:
                        gui.scroll(3000)
                        iters += 1

                    elif iters == len(stone_select(summon_stone)):
                        pass
            sleep(random.uniform(0.5, 0.7))
            gui.click(position)
            sleep(random.uniform(0.5, 1))
            gui.moveTo(random.randrange(591, 705), random.randrange(740, 750), random.uniform(0.8, 1.3))
            gui.click()
            sleep(random.uniform(0.7, 1))

            if gui.locateOnScreen("single_battle/not_api.png", confidence=0.8):
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

            while True:
                sleep(random.uniform(0.5, 1.3))
                if gui.locateOnScreen('single_battle/full.png', confidence=0.7):
                    gui.moveTo(random.randrange(348, 411), random.randrange(480, 484), random.uniform(0.8, 1.3))
                    gui.click()
                    break
                else:
                    print("aaa")
                    pass

            if i == 50:
                break

            while True:
                sleep(random.uniform(0.5, 1.3))
                if gui.locateOnScreen('single_battle/OK.png', confidence=0.7):
                    sleep(random.uniform(0.5, 1.3))
                    close_window()
                    webbrowser.open(quest)
                    break
                else:
                    print("atehamattenaiyto")
                    sleep(5)


partic()
