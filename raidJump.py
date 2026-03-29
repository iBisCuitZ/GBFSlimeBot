import webbrowser
import time
import random
import sys
import pyperclip
import pygetwindow
import pyautogui as auto
import keyboard

TIMEOUT = 15
SCREENSHOT_PATH = r".\Screenshot\\"


def safe_click(coords, duration=0.25):
    """Safely click only if coordinates exist"""
    if coords:
        auto.click(coords, duration=random.uniform(0.01, duration))
        return True
    return False


def wait_for_image(image_name, confidence=0.8, timeout=TIMEOUT):
    """Wait for image with timeout"""
    start_time = time.time()
    while time.time() - start_time < timeout:
        coords = auto.locateCenterOnScreen(
            f"{SCREENSHOT_PATH}{image_name}.PNG", confidence=confidence)
        if coords:
            return coords
        time.sleep(0.3)
    print(f"⚠️ TIMEOUT: {image_name} not found after {timeout}s")
    return None


def attack():
    auto.screenshot()
    check = auto.locateCenterOnScreen(".\Screenshot\\attack.PNG")
    while check is None:
        check = auto.locateCenterOnScreen(".\Screenshot\\attack.PNG")
    auto.click(check, duration=random.uniform(0.01, 0.5))
    time.sleep(1.5)


def quickSummon():
    countdown = 0
    check = auto.locateCenterOnScreen(
        ".\Screenshot\\quickSummon.PNG", confidence=0.9)
    while check is None:
        if countdown <= 5:
            check = auto.locateCenterOnScreen(
                ".\Screenshot\\quickSummon.PNG", confidence=0.9)
            time.sleep(1)
            countdown += 1
        else:
            auto.click(auto.locateCenterOnScreen(
                ".\Screenshot\\reloadBrowser.PNG", confidence=0.9))
            countdown = 0
    auto.click(check, duration=random.uniform(0.01, 0.5))
    time.sleep(2)


def selectSummon(summonName, summonName2):
    print('in Select Summon')
    check = auto.locateCenterOnScreen(
        ".\Screenshot\\"+summonName+".PNG", confidence=0.9)
    check2 = auto.locateCenterOnScreen(
        ".\Screenshot\\"+summonName2+".PNG", confidence=0.9)
    time.sleep(2)
    while check is None and check2 is None:
        auto.scroll(-100)
        check = auto.locateCenterOnScreen(
            ".\Screenshot\\"+summonName+".PNG", confidence=0.9)
        check2 = auto.locateCenterOnScreen(
            ".\Screenshot\\"+summonName2+".PNG", confidence=0.9)
    if check == None:
        auto.click(check2, duration=random.uniform(0.01, 0.5))
    else:
        auto.click(check, duration=random.uniform(0.01, 0.5))

    clickOK()


def clickOK():
    auto.locateCenterOnScreen(".\Screenshot\ok.PNG", confidence=0.9)
    if auto.locateCenterOnScreen(".\Screenshot\ok.PNG", confidence=0.9) != None:
        auto.click(auto.locateCenterOnScreen(".\Screenshot\ok.PNG",
                   confidence=0.9), duration=random.uniform(0.01, 0.5))
    while auto.locateCenterOnScreen(".\Screenshot\ok.PNG", confidence=0.9) is None:
        auto.scroll(-100)
        time.sleep(1)
    time.sleep(3)


def getReward():
    auto.click(auto.locateCenterOnScreen(
        ".\Screenshot\check.PNG", confidence=0.8))
    time.sleep(2)
    auto.moveTo(auto.locateCenterOnScreen(".\Screenshot\pending.PNG"))
    auto.click(auto.move(0, 75))
    time.sleep(2)
    auto.click(auto.locateCenterOnScreen(
        ".\Screenshot\\raidButton.PNG", confidence=0.8))


def fullAuto():
    print("Start Full Auto...")
    wait = 0
    done = 0
    while auto.locateCenterOnScreen(".\Screenshot\\attack.PNG", confidence=0.8) is None and done == 0:
        # Check if the raid is ended. If it's ended go to else. If not check for loop condition (attack button exist)
        if auto.locateCenterOnScreen(".\Screenshot\end.PNG", confidence=0.8) is None and auto.locateCenterOnScreen(".\Screenshot\end2.PNG", confidence=0.8) is None:
            print("CheckFull-AttackLoop")
            time.sleep(1)
            wait += 1
            if wait >= 6:
                auto.click(auto.locateCenterOnScreen(
                    ".\Screenshot\\reload.PNG", confidence=0.7))
                wait = 0
        else:
            print("in else?")
            done = 1
        # time.sleep(3)
        # auto.click(auto.locateCenterOnScreen(".\Screenshot\\attack.PNG",confidence=0.7))
    if done == 0:
        print("BugSure")
        time.sleep(round(random.uniform(0.5, 1), 2))
        auto.click(auto.locateCenterOnScreen(
            ".\Screenshot\\full.PNG", confidence=0.7))
        time.sleep(round(random.uniform(0.5, 1), 2))
    print("BugPa")
    done = 1


def cha1Cast1():
    while auto.locateCenterOnScreen(".\Screenshot\\1st.PNG", confidence=0.7) is None:
        time.sleep(0.5)
    while auto.locateCenterOnScreen(".\Screenshot\\skillInbar.PNG", confidence=0.8) is None:
        auto.click(auto.locateCenterOnScreen(
            ".\Screenshot\\1st.PNG", confidence=0.7))
        time.sleep(0.5)
    auto.moveTo(auto.locateCenterOnScreen(
        ".\Screenshot\skillInBar.PNG", confidence=0.7))
    time.sleep(0.5)
    auto.click(auto.move(30, 30))
    auto.click(auto.locateCenterOnScreen(
        ".\Screenshot\\backButton.PNG", confidence=0.7))
    time.sleep(0.1)


def cha1Cast2():
    while auto.locateCenterOnScreen(".\Screenshot\\1st.PNG", confidence=0.7) is None:
        time.sleep(0.5)
    while auto.locateCenterOnScreen(".\Screenshot\\skillInbar.PNG", confidence=0.8) is None:
        auto.click(auto.locateCenterOnScreen(
            ".\Screenshot\\1st.PNG", confidence=0.7))
        time.sleep(0.5)
    auto.moveTo(auto.locateCenterOnScreen(
        ".\Screenshot\skillInBar.PNG", confidence=0.7))
    time.sleep(0.5)
    auto.click(auto.move(120, 30))
    auto.click(auto.locateCenterOnScreen(
        ".\Screenshot\\backButton.PNG", confidence=0.7))
    time.sleep(0.1)


def cha2Cast1():
    while auto.locateCenterOnScreen(".\Screenshot\\2nd.PNG", confidence=0.7) is None:
        time.sleep(0.5)
    while auto.locateCenterOnScreen(".\Screenshot\\skillInbar.PNG", confidence=0.8) is None:
        auto.click(auto.locateCenterOnScreen(
            ".\Screenshot\\2nd.PNG", confidence=0.7))
        time.sleep(0.5)
    auto.moveTo(auto.locateCenterOnScreen(
        ".\Screenshot\skillInBar.PNG", confidence=0.7))
    time.sleep(0.5)
    auto.click(auto.move(30, 30))
    time.sleep(1)
    auto.click(auto.locateCenterOnScreen(
        ".\Screenshot\\backButton.PNG", confidence=0.7))
    time.sleep(0.5)


def cha3Cast1():
    while auto.locateCenterOnScreen(".\Screenshot\\3rd.PNG", confidence=0.7) is None:
        time.sleep(0.5)
    while auto.locateCenterOnScreen(".\Screenshot\\skillInbar.PNG", confidence=0.8) is None:
        auto.click(auto.locateCenterOnScreen(
            ".\Screenshot\\3rd.PNG", confidence=0.7))
        time.sleep(0.5)
    auto.moveTo(auto.locateCenterOnScreen(
        ".\Screenshot\skillInBar.PNG", confidence=0.7))
    time.sleep(0.5)
    auto.click(auto.move(30, 30))
    time.sleep(1)
    auto.click(auto.locateCenterOnScreen(
        ".\Screenshot\\backButton.PNG", confidence=0.7))
    time.sleep(0.5)


def cha3Cast2():
    while auto.locateCenterOnScreen(".\Screenshot\\3rd.PNG", confidence=0.7) == None:
        time.sleep(0.5)
    time.sleep(1)
    while auto.locateCenterOnScreen(".\Screenshot\\skillInbar.PNG", confidence=0.8) is None:
        auto.click(auto.locateCenterOnScreen(
            ".\Screenshot\\3rd.PNG", confidence=0.7))
        time.sleep(0.5)
    auto.moveTo(auto.locateCenterOnScreen(
        ".\Screenshot\skillInBar.PNG", confidence=0.7))
    time.sleep(0.5)
    auto.click(auto.move(100, 30))
    time.sleep(1)
    auto.click(auto.locateCenterOnScreen(
        ".\Screenshot\\backButton.PNG", confidence=0.7))
    time.sleep(0.5)


def cha3Cast3():
    while auto.locateCenterOnScreen(".\Screenshot\\3rd.PNG", confidence=0.7) == None:
        time.sleep(0.5)
    time.sleep(1)
    while auto.locateCenterOnScreen(".\Screenshot\\skillInbar.PNG", confidence=0.8) is None:
        auto.click(auto.locateCenterOnScreen(
            ".\Screenshot\\3rd.PNG", confidence=0.7))
        time.sleep(0.5)
    auto.moveTo(auto.locateCenterOnScreen(
        ".\Screenshot\skillInBar.PNG", confidence=0.7))
    time.sleep(0.5)
    auto.click(auto.move(180, 30))
    time.sleep(1)
    auto.click(auto.locateCenterOnScreen(
        ".\Screenshot\\backButton.PNG", confidence=0.7))
    time.sleep(0.5)


def back():
    print("click back button")
    auto.click(auto.locateCenterOnScreen(".\Screenshot\\back.PNG"))


def reload():
    auto.click(auto.locateCenterOnScreen(f"{SCREENSHOT_PATH}reload.PNG"))
    time.sleep(2)


def summonCall(summon):
    check = wait_for_image("summonTab", confidence=0.8, timeout=10)
    safe_click(check, duration=0.25)
    time.sleep(2)

    check = wait_for_image(f"{summon}Call", confidence=0.8, timeout=10)
    safe_click(check, duration=0.25)
    clickOK()


# ========= Option =========#
callSummon = "huanglong"
callSummon2 = "agni2"
run = 300000
i = 0
joined = 0

while i != run:
    if auto.locateCenterOnScreen(f"{SCREENSHOT_PATH}check.PNG") != None:
        while auto.locateCenterOnScreen(f"{SCREENSHOT_PATH}check.PNG") != None:
            getReward()
            time.sleep(1)
    elif joined != 3:
        # Check for noRaid.PNG at cursor
        no_raid = auto.locateCenterOnScreen(
            f"{SCREENSHOT_PATH}noRaid.PNG", confidence=0.8)

        while (no_raid):
            print("No raid found, reloading...")
            reload_btn = auto.locateCenterOnScreen(
                f"{SCREENSHOT_PATH}raidReload.PNG", confidence=0.8)
            time.sleep(2)
            safe_click(reload_btn, duration=0.25)
            print("Reloaded, checking again...")
            time.sleep(1)
            no_raid = auto.locateCenterOnScreen(
                f"{SCREENSHOT_PATH}noRaid.PNG", confidence=0.8)
            if (no_raid is None):
                print("Raid found!")
                break
            else:
                print("Still no raid, waiting before next reload...")
                time.sleep(5)
        auto.moveTo(auto.locateCenterOnScreen(
            f"{SCREENSHOT_PATH}raidScreenAnchor.PNG", confidence=0.8))
        time.sleep(0.5)
        auto.click(auto.move(-50, 200))
        time.sleep(0.5)
        print('move fin')
        # LEGACY
        # ========GameClients==========#
        # print("click enterID")
        # auto.click(auto.locateCenterOnScreen(".\Screenshot\\enterID.PNG",confidence=0.9))
        # time.sleep(1)
        # print("click Join a room")
        # auto.moveTo(auto.locateCenterOnScreen(".\Screenshot\\joinARoom.PNG",confidence=0.7))
        # print("move down")
        # auto.click(auto.move(-240,0))
        # time.sleep(1)
        # print("pasted")
        # # auto.hotkey('ctrl','v')
        # keyboard.press_and_release('ctrl+v')
        # time.sleep(1)
        # print('click join')
        # auto.click(auto.locateCenterOnScreen(".\Screenshot\\joinARoom.PNG",confidence=0.7))
        raidNoti = auto.locateCenterOnScreen(
            f"{SCREENSHOT_PATH}raidNoti.PNG", confidence=0.9)
        battleNoti = auto.locateCenterOnScreen(
            f"{SCREENSHOT_PATH}battleNoti.PNG", confidence=0.9)
        noroom = auto.locateCenterOnScreen(
            f"{SCREENSHOT_PATH}noroom.PNG", confidence=0.9)

        if not raidNoti and not battleNoti and not noroom:
            print("Joining")
            time.sleep(1)
            clickOK()
            time.sleep(1)

            # Re-check images AFTER clickOK
            raidNoti = auto.locateCenterOnScreen(
                f"{SCREENSHOT_PATH}raidNoti.PNG", confidence=0.9)
            battleNoti = auto.locateCenterOnScreen(
                f"{SCREENSHOT_PATH}battleNoti.PNG", confidence=0.9)
            noroom = auto.locateCenterOnScreen(
                f"{SCREENSHOT_PATH}noroom.PNG", confidence=0.9)

            print("Check raidNoti, battleNoti, noroom after clickOK joining")
            if not raidNoti and not battleNoti and not noroom:
                print("Fight")
                fullAuto()
                time.sleep(40)
                fullAuto()
                time.sleep(20)
                auto.click(auto.locateCenterOnScreen(
                    f"{SCREENSHOT_PATH}raidButton.PNG", confidence=0.8))
                # cha1Cast1()
                # time.sleep(0.8)
                # cha1Cast2()
                # time.sleep(0.8)
                # quickSummon()
                # attack()
                time.sleep(1)
                auto.click(auto.locateCenterOnScreen(
                    ".\Screenshot\\raidButton.PNG", confidence=0.8))
                auto.move(0, 50)
                if auto.locateCenterOnScreen(".\Screenshot\check.PNG") != None:
                    while auto.locateCenterOnScreen(".\Screenshot\check.PNG") != None:
                        getReward()
                        time.sleep(1)
                time.sleep(2)
                joined = len(
                    list(auto.locateAllOnScreen(".\Screenshot\joined.PNG")))
                print(joined)
                print("FightEND")
        else:
            print("in Reload")
            auto.click(auto.locateCenterOnScreen(
                ".\Screenshot\\refresh.PNG", confidence=0.8))
            auto.click(auto.locateCenterOnScreen(
                ".\Screenshot\\raidButton.PNG", confidence=0.8))
            auto.move(0, 50)
            time.sleep(5)
    else:
        time.sleep(10)
        # while joined == 3:
        #     if auto.locateCenterOnScreen(".\Screenshot\check.PNG") != None:
        #         while auto.locateCenterOnScreen(".\Screenshot\check.PNG") != None:
        #             getReward()
        #             time.sleep(1)
        #     print ("Check Dupe")
        #     auto.hotkey('f5')
        #     time.sleep(5)
        #     auto.scroll(-100)
        #     joined = len(list(auto.locateAllOnScreen(".\Screenshot\joined.PNG")))
