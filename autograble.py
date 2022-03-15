import webbrowser
import requests
import pyautogui as gui
import random
from time import sleep
from components import summon_stone
from components.gui_grable import grable_gui
from components import single_play


def unclaimed():
    while True:
        sleep(2)
        if gui.locateOnScreen("multi_battle/unclaimed.png", confidence=0.8):
            gui.moveTo(random.randrange(249, 380), random.randrange(307, 745), random.uniform(0.6, 1))
            gui.click()
            sleep(1.5)
            webbrowser.open("http://game.granbluefantasy.jp/#quest/assist/unclaimed")
        else:
            break


def close_window():
    import pyautogui
    pyautogui.keyDown('ctrl')
    pyautogui.press('w')
    pyautogui.keyUp('ctrl')
    return


# inputデータを消す用
def delete_word():
    import pyautogui
    pyautogui.keyDown('ctrl')
    pyautogui.press('a')
    pyautogui.keyUp('ctrl')
    pyautogui.press('esc')
    return


def api_write():
    res = requests.get('http://127.0.0.1:8888/')
    res = res.json()["war_code"]
    gui.write(res)


def input_word():
    gui.moveTo(random.randrange(398, 542), random.randrange(551, 565), random.uniform(0.8, 1.3))
    gui.click()
    sleep(random.uniform(0.3, 1))


def assign():
    gui.moveTo(random.randrange(609, 724), random.randrange(541, 560), random.uniform(0.8, 1.3))
    gui.click()
    sleep(random.uniform(0.5, 1))


def daily_routine():
    quest = {
        "magna_ex": "http://game.granbluefantasy.jp/#quest/supporter/305261/28",
        "angel_pro": "http://game.granbluefantasy.jp/#quest/supporter/305301/28",
        "tiamat_magna": "http://game.granbluefantasy.jp/#quest/supporter/305081/1/0/18",
        "koro_magna": "http://game.granbluefantasy.jp/#quest/supporter/305091/1/0/19",
        "riva_magna": "http://game.granbluefantasy.jp/#quest/supporter/305101/1/0/20",
        "yugu_magna": "http://game.granbluefantasy.jp/#quest/supporter/305101/1/0/21",
        "syuva_magna": "http://game.granbluefantasy.jp/#quest/supporter/305121/1/0/26",
        "selest_magna": "http://game.granbluefantasy.jp/#quest/supporter/305131/1/0/31"
    }


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


def multi_battle():
    stone_genre = values[0]
    element = values[1]
    i = 0
    count = 0
    iters = 1

    while True:
        i += 1
        webbrowser.open("http://game.granbluefantasy.jp/#quest/assist")
        sleep(2)
        gui.moveTo(random.randrange(674, 795), random.randrange(276, 310), random.uniform(0.8, 1.3))
        gui.click()
        input_word()
        api_write()
        assign()
        while True:
            if gui.locateOnScreen('multi_battle/end_battle.png', confidence=0.9) or gui.locateOnScreen(
                    'multi_battle/notfound.png', confidence=0.9):
                gui.moveTo(random.randrange(500, 598), random.randrange(618, 650), random.uniform(0.8, 1))
                gui.click()
                sleep(10)
                input_word()
                delete_word()
                api_write()
                assign()
            elif gui.locateOnScreen('multi_battle/multi_battle_limit.png', confidence=0.9):
                sleep(30)
            elif gui.locateOnScreen('multi_battle/unclaimed.png', confidence=0.9):
                unclaimed()
            else:
                break

        if gui.locateOnScreen('multi_battle/Nothing_AP.png', confidence=0.9):
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
            if gui.locateOnScreen(summon_stone[stone_genre][element][str(iters)], confidence=0.9):
                position = gui.locateOnScreen(summon_stone[stone_genre][element][str(iters)],
                                              confidence=0.9)
                gui.click(position)
                sleep(random.uniform(0.3, 1))
                break
            else:
                count += 1
                gui.scroll(-600)
                sleep(random.uniform(0.3, 1))
                if iters == len(summon_stone[stone_genre][element]):
                    gui.moveTo(random.randrange(379, 679), random.randrange(740, 771), random.uniform(0.5, 1.0))
                    gui.click()
                    sleep(random.uniform(0.3, 1))
                    break
                if count >= 5:
                    gui.scroll(3000)
                    iters += 1
                    count = 0

        gui.moveTo(random.randrange(591, 705), random.randrange(740, 750), random.uniform(0.8, 1.3))
        sleep(random.uniform(0.3, 1))
        gui.click()

        while True:
            if gui.locateOnScreen('multi_battle/full.png', confidence=0.6) or gui.locateOnScreen(
                    'multi_battle/gard_full.png',
                    confidence=0.6):
                gui.moveTo(random.randrange(348, 411), random.randrange(480, 484), random.uniform(0.8, 1.3))
                gui.click()

                break
            else:
                pass
        print(values[3])
        if i == int(values[3]):
            break

        while True:
            if gui.locateOnScreen('multi_battle/result.png', confidence=0.7):
                gui.moveTo(random.randrange(498, 666), random.randrange(642, 658), random.uniform(0.8, 1.3))
                gui.click()
                sleep(5)
                close_window()
                break
            elif gui.locateOnScreen('multi_battle/battle_completed.png', confidence=0.7):
                close_window()
                break
            elif gui.locateOnScreen('multi_battle/lose_icon.png', confidence=0.7):
                close_window()
                break
            elif gui.locateOnScreen('multi_battle/lose_icon1.png', confidence=0.7):
                close_window()
                break
            elif gui.locateOnScreen('multi_battle/lose_icon2.png', confidence=0.7):
                close_window()
                break
            elif gui.locateOnScreen('multi_battle/lose_icon3.png', confidence=0.7):
                close_window()
                break
            elif gui.locateOnScreen('multi_battle/lose_icon.png4', confidence=0.7):
                close_window()
                break
            elif gui.locateOnScreen('multi_battle/lose.png', confidence=0.7):
                close_window()
                break
            else:
                sleep(5)


values = grable_gui()

# 0 = 召喚石ジャンル, 1 = 召喚石属性, 2 = 周回回数, 3 = クエストURL : ボス, 4 = モード
values = values[0], values[1], values[2], values[3], values[4]
summon_stone = summon_stone.summon_stone()

if values[4] == "single":
    single_play.single_play(values, summon_stone)
else:
    multi_battle()
