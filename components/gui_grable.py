import PySimpleGUI as sg


def grable_gui():
    sg.theme('DarkAmber')
    select_summon_stone = '召喚石の種類を選択してください'
    select_summon_element = '召喚石の属性を選択してください'
    auto_count = '自動で何周回するか入力してください'
    input_quest = 'クエストのURLを入力してください'
    multi_boss_select = "周回するボスを選択してください"

    single_play = [[sg.Text('グラブル自動化ツール')],
                   [sg.Text(select_summon_stone),
                    sg.Listbox(["神石", "マグナ石", "プロビデンス"], size=(25, 3))],
                   [sg.Text(select_summon_element),
                    sg.Listbox(["火", "水", "土", "風", "光", "闇"], size=(25, 6))],
                   [sg.Text(auto_count),
                    sg.InputText(size=(5, 1))],
                   [sg.Text(input_quest),
                    sg.InputText(size=(50, 1))],
                   [sg.Button('OK', key="single_ok"), sg.Button('キャンセル', key="single_close")]]  # 幅,高

    multi_play = [[sg.Text('グラブル自動化ツール')],
                  [sg.Text(select_summon_stone),
                   sg.Listbox(["神石", "マグナ石", "プロビデンス"], size=(25, 3))],
                  [sg.Text(select_summon_element),
                   sg.Listbox(["火", "水", "土", "風", "光", "闇"], size=(25, 6))],
                  [sg.Text(multi_boss_select),
                   sg.Listbox(["シヴァ", "エウロペ", "ブローディア", "グリームニル", "メタトロン", "アバター"], size=(25, 6))],
                  [sg.Text(auto_count),
                   sg.InputText(size=(5, 1))],
                  [sg.Button('OK', key="multi_ok"), sg.Button('キャンセル', key="multi_close")]]  # 幅,高さ

    start_display = [[sg.TabGroup(
        [[sg.Tab('クエストモード', single_play, key="single"), sg.Tab('救援モード', multi_play, key="multi")]], key="tab_group")]]
    window = sg.Window("グラブル自動化", start_display, default_element_size=(22, 3))

    # GUI表示実行部分

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'multi_close' or event == "single_close":
            break

        # ボタンがOKなら一つめのinputが選択してくださいではない且つ２つ目も３つ目も
        if event == 'single_ok' and values[0] != "選択してください" and values[1] != "選択してください" and values[2] != "" and values[
            3] != "":
            summon = values[0]
            select_tab = values["tab_group"]
            # value[0]にメインプログラムで動かすキー名にしたいため英文字で再代入
            if summon[0] == "神石":
                values[0] = "god"
            elif summon[0] == "マグナ石":
                values[0] = "magna"
            elif summon[0] == "プロビデンス":
                values[0] = "provi"
            element = values[1]
            if element[0] == "火":
                values[1] = "fire"
            elif element[0] == "水":
                values[1] = "water"
            elif element[0] == "風":
                values[1] = "wind"
            elif element[0] == "土":
                values[1] = "sand"
            elif element[0] == "光":
                values[1] = "light"
            elif element[0] == "闇":
                values[1] = "dark"
            values[4] = select_tab
            return values[0], values[1], values[2], values[3], values[4], window.close()
        elif event == 'single_ok' and values[0] == []:
            sg.popup(select_summon_stone)
        elif event == 'single_ok' and values[1] == []:
            sg.popup(select_summon_element)
        elif event == 'single_ok' and values[2] == "":
            sg.popup("回数が入力されていません" + "\n" + "入力してください")
        elif event == 'single_ok' and values[3] == "":
            sg.popup("クエストURLが入力されていません" + "\n" + "入力してください")

        if event == 'multi_ok' and values[4] != [] and values[5] != [] and values[6] != [] and values[7] != "":
            summon = values[4]
            select_tab = values["tab_group"]
            if summon[0] == "神石":
                values[0] = "god"
            elif summon[0] == "マグナ石":
                values[0] = "magna"
            elif summon[0] == "プロビデンス":
                values[0] = "provi"
            element = values[5]
            if element[0] == "火":
                values[1] = "fire"
            elif element[0] == "水":
                values[1] = "water"
            elif element[0] == "風":
                values[1] = "wind"
            elif element[0] == "土":
                values[1] = "sand"
            elif element[0] == "光":
                values[1] = "light"
            elif element[0] == "闇":
                values[1] = "dark"
            boss = values[6]
            if boss[0] == "シヴァ":
                values[2] = "shiva"
            elif boss[0] == "エウロペ":
                values[2] = "europe"
            elif boss[0] == "グリームニル":
                values[2] = "grimnil"
            elif boss[0] == "ブローディア":
                values[2] = "browdia"
            elif boss[0] == "メタトロン":
                values[2] = "meta"
            elif boss[0] == "アバター":
                values[2] = "avatar"
            values[3] = values[7]
            values[4] = select_tab
            return values[0], values[1], values[2], values[3], values[4], window.close()

        elif event == 'multi_ok' and values[4] == []:
            sg.popup(select_summon_stone)
        elif event == 'multi_ok' and values[5] == []:
            sg.popup(select_summon_element)
        elif event == 'multi_ok' and values[6] == []:
            sg.popup("周回するボスを選択してください")
        elif event == 'multi_ok' and values[7] == "":
            sg.popup("回数が入力されていません" + "\n" + "入力してください")

