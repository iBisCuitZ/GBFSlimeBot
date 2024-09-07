import pyautogui as auto
import webbrowser
import time
import random
import sys
import pygetwindow


def refillButton():
    while auto.locateCenterOnScreen(".\Screenshot\\refillMenu.png", confidence=0.9) is None:
        time.sleep(0.5)
    auto.click(auto.locateCenterOnScreen(
        ".\Screenshot\\refillMenu.PNG", confidence=0.7),duration=random.uniform(0.2,2))
    time.sleep(0.1)

def sortieButton():
    while auto.locateCenterOnScreen(".\Screenshot\\sortieButton.png", confidence=0.9) is None:
        time.sleep(0.5)
    auto.click(auto.locateCenterOnScreen(
        ".\Screenshot\\sortieButton.PNG", confidence=0.9),duration=random.uniform(0.2,2))
    time.sleep(0.1)

def mainButton():
    while auto.locateCenterOnScreen(".\Screenshot\\mainButton.png", confidence=0.9) is None:
        time.sleep(0.5)
    auto.click(auto.locateCenterOnScreen(
        ".\Screenshot\\mainButton.PNG", confidence=0.7),duration=random.uniform(0.2,2))
    time.sleep(0.1)


def world74():
    while auto.locateCenterOnScreen(".\Screenshot\\world7.png", confidence=0.9) is None:
        time.sleep(0.5)
    auto.click(auto.locateCenterOnScreen(
        ".\Screenshot\\world7.PNG", confidence=0.9),duration=random.uniform(0.2,2))
    time.sleep(2)
    auto.click(auto.locateCenterOnScreen(
        ".\Screenshot\\world74.PNG", confidence=0.9),duration=random.uniform(0.2,2))
    time.sleep(1)
    auto.click(auto.locateCenterOnScreen(
        ".\Screenshot\\startSortie.PNG", confidence=0.9),duration=random.uniform(0.2,2))   
    time.sleep(1)
    auto.click(auto.locateCenterOnScreen(
        ".\Screenshot\\startSortie2.PNG", confidence=0.9),duration=random.uniform(0.2,2))

def backHome():
    auto.moveTo(auto.locateCenterOnScreen(
        ".\Screenshot\\name.PNG", confidence=0.7))
    time.sleep(0.5)
    auto.click(auto.move(-150, 00,duration=random.uniform(0.2,2)))
    time.sleep(1)
    auto.click(auto.locateCenterOnScreen(
        ".\Screenshot\\backButton.PNG", confidence=0.7))
    time.sleep(0.5)

def loopClick():
    auto.click(500,500)

def checkSelectPath():
    auto.moveTo(auto.locateCenterOnScreen(".\Screenshot\\74jnode.PNG", confidence=0.9),duration=random.uniform(0.2,2))
    auto.click(auto.move(180,-45),duration=random.uniform(0.2,2))

# ======================== Setting ==============================

# How many run
count = 30

# ===============================================================
i = 0
while i < count:
    win = pygetwindow.getWindowsWithTitle('艦隊これくしょん -艦これ- - オンラインゲーム - DMM GAMES')[0]
    win.activate()
    # === Refill ===
    refillButton()
    time.sleep(2)
    auto.click(auto.locateCenterOnScreen(".\Screenshot\\refill.PNG", confidence=0.9),duration=random.uniform(0.2,2))
    time.sleep(2)
    backHome()
    # ==============
    time.sleep(3)
    mainButton()
    auto.move(-150, 00,)
    sortieButton()
    time.sleep(1)

    # ===== Select World =====
    world74()

    while(auto.locateCenterOnScreen(".\Screenshot\\7-4routeSelect.png", confidence=0.9) is None):
        loopClick()
        time.sleep(random.randint(3,7))
    checkSelectPath()
    while(auto.locateCenterOnScreen(".\Screenshot\\mainButton.png", confidence=0.9) is None):
        loopClick()
        time.sleep(random.randint(3,7))
    # ========================
    i += 1
    sys.stdout.write("Round "+str(i)+" Finished\n")
