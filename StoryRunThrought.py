import pyautogui as auto
import webbrowser
import time
import random
import sys
import pygetwindow
import winsound

TIMEOUT = 15
SCREENSHOT_PATH = r".\Screenshot\\"


def play_verification_alarm():
    """Play alarm repeatedly while verification screen is visible."""
    print("⚠️ verification.PNG detected - alarm loop started")
    while auto.locateCenterOnScreen(".\Screenshot\\verification.PNG", confidence=0.8) is not None:
        winsound.Beep(1200, 450)
        time.sleep(0.1)


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
        time.sleep(0.15)
    print(f"⚠️ TIMEOUT: {image_name} not found after {timeout}s")
    return None


def macroButton():
    auto.click(auto.locateCenterOnScreen(
        ".\Screenshot\\macroButton.png", confidence=0.9))


def selectSummon(summonName):
    check = auto.locateCenterOnScreen(".\Screenshot\\"+summonName+".PNG")
    print("in selectSummon()")
    if check != None:
        auto.click(check, duration=random.uniform(0.01, 0.3))
    else:
        while check == None:
            auto.scroll(-200)
            time.sleep(0.5)
            check = auto.locateCenterOnScreen(
                ".\Screenshot\\"+summonName+".PNG", confidence=0.8)
    auto.click(check, duration=random.uniform(0.01, 0.3))
    auto.click(check)


def clickOK():
    check = auto.locateCenterOnScreen(".\Screenshot\ok.PNG", confidence=0.8)
    if check != None:
        auto.click(check, duration=random.uniform(0.01, 0.5))
    while check is None:
        auto.scroll(-100)
        time.sleep(0.1)
        check = auto.locateOnScreen(".\Screenshot\ok.PNG", confidence=0.8)
    auto.click(check, duration=random.uniform(0.01, 0.5))


def clickSkip():
    while auto.locateCenterOnScreen(".\Screenshot\loading.PNG", confidence=0.8) is not None:
        time.sleep(0.1)
    check = auto.locateCenterOnScreen(
        ".\Screenshot\skipButton.PNG", confidence=0.8)
    if check != None:
        auto.click(check, duration=random.uniform(0.01, 0.5))
    while check is None:
        auto.scroll(-100)
        time.sleep(0.1)
        check = auto.locateOnScreen(
            ".\Screenshot\skipButton.PNG", confidence=0.8)
    auto.click(check, duration=random.uniform(0.01, 0.5))


def clickSkipBlue():
    check = auto.locateCenterOnScreen(
        ".\Screenshot\skipButtonBlue.PNG", confidence=0.8)
    if check != None:
        auto.click(check, duration=random.uniform(0.01, 0.5))
    while check is None:
        auto.scroll(-100)
        time.sleep(0.1)
        check = auto.locateOnScreen(
            ".\Screenshot\skipButtonBlue.PNG", confidence=0.8)
    auto.click(check, duration=random.uniform(0.01, 0.5))


def summonCall(summon):
    # Wait for summonTab with timeout, click refresh if not found
    check = wait_for_image("summonTab", confidence=0.8, timeout=10)
    if not check:
        print("summonTab not found, clicking refresh...")
        refresh = auto.locateCenterOnScreen(
            f"{SCREENSHOT_PATH}refresh.PNG", confidence=0.8)
        if refresh:
            safe_click(refresh, duration=0.25)
            time.sleep(1)
        check = wait_for_image("summonTab", confidence=0.8, timeout=20)
    time.sleep(0.5)
    safe_click(check, duration=0.25)
    time.sleep(1)

    # Wait for summonCall button
    check = wait_for_image(f"{summon}Call", confidence=0.8, timeout=20)
    safe_click(check, duration=0.25)

    clickOK()


def attack():
    count = 0
    check = auto.locateCenterOnScreen(
        ".\Screenshot\\attack.PNG", confidence=0.9)
    while check is None:
        verification = auto.locateCenterOnScreen(
            ".\Screenshot\\verification.PNG", confidence=0.8)
        if verification is not None:
            play_verification_alarm()
        if (count % 5 == 0):
            print("check attack")
        check = auto.locateCenterOnScreen(
            ".\Screenshot\\attack.PNG", confidence=0.9)
        count += 1
    auto.click(check, duration=random.uniform(0.01, 0.5))
    time.sleep(0.5)


def back():
    print("press back")
    auto.click(auto.locateCenterOnScreen(
        ".\Screenshot\\back.PNG", confidence=0.8))
    time.sleep(1)


def waitForRaidEnd():
    """Wait for raid to end, click attack if available"""
    start_time = time.time()
    timeout = 300  # 5 minutes max

    while time.time() - start_time < timeout:
        # Check if attack button exists and click it
        attack_coords = auto.locateCenterOnScreen(
            ".\Screenshot\\attack.PNG", confidence=0.9)
        next_coords = auto.locateCenterOnScreen(
            ".\Screenshot\\next.PNG", confidence=0.8)
        if attack_coords:
            safe_click(attack_coords, duration=0.25)
            time.sleep(1)
            continue
        if next_coords:
            safe_click(next_coords, duration=0.25)
            time.sleep(1)
            continue
        # Check if raid ended
        end_coords = auto.locateCenterOnScreen(
            ".\Screenshot\\end.PNG", confidence=0.8)
        if end_coords:
            print("✓ Raid ended")
            return
        time.sleep(0.25)
        print("waiting to end...")
    print(f"⚠️ TIMEOUT: Raid didn't end after {timeout}s")


def cha1Cast1():
    print("1start")
    while auto.locateCenterOnScreen(".\Screenshot\\1st.PNG", confidence=0.7) == None:
        time.sleep(0.25)
    time.sleep(0.5)
    auto.click(auto.locateCenterOnScreen(
        ".\Screenshot\\1st.PNG", confidence=0.7))
    time.sleep(0.25)
    auto.moveTo(auto.locateCenterOnScreen(
        ".\Screenshot\skillInBar.PNG", confidence=0.7))
    auto.click(auto.move(30, 30))
    time.sleep(0.25)
    auto.click(auto.locateCenterOnScreen(".\Screenshot\\backButton.PNG"))
    time.sleep(0.25)
    print("1end")


def cha1Cast2():
    print("12start")
    while auto.locateCenterOnScreen(".\Screenshot\\1st.PNG", confidence=0.7) == None:
        time.sleep(0.25)
    time.sleep(0.5)
    auto.click(auto.locateCenterOnScreen(
        ".\Screenshot\\1st.PNG", confidence=0.7))
    time.sleep(0.25)
    auto.moveTo(auto.locateCenterOnScreen(
        ".\Screenshot\skillInBar.PNG", confidence=0.7))
    auto.click(auto.move(100, 30))
    time.sleep(0.25)
    auto.click(auto.locateCenterOnScreen(".\Screenshot\\backButton.PNG"))
    time.sleep(0.25)
    print("12end")


def cha1Cast3():
    print("13start")
    while auto.locateCenterOnScreen(".\Screenshot\\1st.PNG", confidence=0.7) == None:
        time.sleep(0.25)
    time.sleep(0.5)
    auto.click(auto.locateCenterOnScreen(
        ".\Screenshot\\1st.PNG", confidence=0.7))
    time.sleep(0.25)
    auto.moveTo(auto.locateCenterOnScreen(
        ".\Screenshot\skillInBar.PNG", confidence=0.7))
    auto.click(auto.move(180, 30))
    time.sleep(0.25)
    auto.click(auto.locateCenterOnScreen(
        ".\Screenshot\\backButton.PNG", confidence=0.9))
    time.sleep(0.25)
    print("13end")


def cha1Cast4():
    while auto.locateCenterOnScreen(".\Screenshot\\1st.PNG", confidence=0.7) == None:
        time.sleep(0.25)
    time.sleep(0.5)
    auto.click(auto.locateCenterOnScreen(
        ".\Screenshot\\1st.PNG", confidence=0.7))
    time.sleep(0.25)
    auto.moveTo(auto.locateCenterOnScreen(
        ".\Screenshot\skillInBar.PNG", confidence=0.7))
    auto.click(auto.move(270, 30))
    time.sleep(0.25)
    auto.click(auto.locateCenterOnScreen(".\Screenshot\\backButton.PNG"))
    time.sleep(0.25)


def cha2Cast1():
    print("21start")
    while auto.locateCenterOnScreen(".\Screenshot\\2nd.PNG", confidence=0.7) is None:
        time.sleep(0.25)
    while auto.locateCenterOnScreen(".\Screenshot\\skillInbar.PNG", confidence=0.8) is None:
        auto.click(auto.locateCenterOnScreen(
            ".\Screenshot\\2nd.PNG", confidence=0.7))
        time.sleep(0.25)
    auto.moveTo(auto.locateCenterOnScreen(
        ".\Screenshot\skillInBar.PNG", confidence=0.7))
    auto.click(auto.move(30, 30))
    time.sleep(0.25)
    while auto.locateCenterOnScreen(".\Screenshot\\backButton.PNG", confidence=0.7) != None:
        auto.click(auto.locateCenterOnScreen(
            ".\Screenshot\\backButton.PNG", confidence=0.7))
    time.sleep(0.25)
    print("21end")


def cha3Cast1():
    print("31start")
    while auto.locateCenterOnScreen(".\Screenshot\\3rd.PNG", confidence=0.7) is None:
        time.sleep(0.25)
    while auto.locateCenterOnScreen(".\Screenshot\\skillInbar.PNG", confidence=0.8) is None:
        auto.click(auto.locateCenterOnScreen(
            ".\Screenshot\\3rd.PNG", confidence=0.7))
        time.sleep(0.25)
    auto.moveTo(auto.locateCenterOnScreen(
        ".\Screenshot\skillInBar.PNG", confidence=0.7))
    auto.click(auto.move(30, 30))
    time.sleep(0.25)
    auto.click(auto.locateCenterOnScreen(".\Screenshot\\backButton.PNG"))
    time.sleep(0.25)
    print("31end")


def cha3Cast2():
    print("32start")
    while auto.locateCenterOnScreen(".\Screenshot\\3rd.PNG", confidence=0.7) == None:
        time.sleep(0.25)
    time.sleep(0.5)
    while auto.locateCenterOnScreen(".\Screenshot\\skillInbar.PNG", confidence=0.8) is None:
        auto.click(auto.locateCenterOnScreen(
            ".\Screenshot\\3rd.PNG", confidence=0.7))
        time.sleep(0.25)
    auto.moveTo(auto.locateCenterOnScreen(
        ".\Screenshot\skillInBar.PNG", confidence=0.7))
    auto.click(auto.move(100, 30))
    time.sleep(0.25)
    auto.click(auto.locateCenterOnScreen(
        ".\Screenshot\\backButton.PNG", confidence=0.7))
    time.sleep(0.25)
    print("32end")


def fullAuto():
    wait = 0
    while auto.locateCenterOnScreen(".\Screenshot\\attack.PNG", confidence=0.7) is None:
        print("CheckFull-AttackLoop")
        time.sleep(0.5)
        wait += 1
        if wait >= 6:
            print("waited: "+str(wait))
            auto.click(auto.locateCenterOnScreen(
                ".\Screenshot\\reload.PNG", confidence=0.7))
            wait = 0
    # time.sleep(3)
    # auto.click(auto.locateCenterOnScreen(".\Screenshot\\attack.PNG",confidence=0.7))
    time.sleep(round(random.uniform(0.5, 1), 2) / 2)
    auto.click(auto.locateCenterOnScreen(
        ".\Screenshot\\full.PNG", confidence=0.7))
    time.sleep(round(random.uniform(0.5, 1), 2) / 2)


def getGem():
    while auto.locateCenterOnScreen(".\\test\\gem.png", confidence=0.9) is None:
        time.sleep(1)
        auto.scroll(-200)
    auto.click(auto.locateCenterOnScreen(
        ".\\test\\gem.png", confidence=0.9))


# ======================== Setting ==============================
# Summon to call
summon = "huanglong"
# How many run
count = 404040
# Link
fight = 'http://game.granbluefantasy.jp/#quest/supporter/400181/4'
# ============================================================
i = 0
while i <= count:
    sys.stdout.write("Running Round "+str(i+1)+"\n")
    win = pygetwindow.getWindowsWithTitle('Granblue Fantasy')[0]
    win.activate()
    # while auto.locateCenterOnScreen(".\Screenshot\\vee.PNG",confidence=0.8) == None:
    #     auto.locateCenterOnScreen(".\Screenshot\\vee.PNG",confidence=0.8)
    # auto.click(auto.locateCenterOnScreen(".\Screenshot\\vee.PNG",confidence=0.8),clicks=2)
    # selectSummon(summon)
    # print("TO CLICK OK")
    # clickOK()
    # time.sleep(2)
    # print("TO CLICK SKIP")
    # clickSkip()
    # time.sleep(0.5)
    # print("TO CLICK SKIP BLUE")
    # clickSkipBlue()
    # time.sleep(0.5)
    getGem()
    time.sleep(3)
    clickSkip()
    clickSkipBlue()
    time.sleep(2)
    macroButton()
    # ============================= Fight END ================#
    i += 1
    sys.stdout.write("Round "+str(i)+" Finished\n")
