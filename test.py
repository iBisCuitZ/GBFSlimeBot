import pyautogui as auto
import pygetwindow,time

auto.moveTo(auto.locateCenterOnScreen(".\Screenshot\\ifritNM.PNG",confidence=0.8))
print("move down")
auto.click(auto.move(275,30))
time.sleep(0.5)
auto.click(auto.locateCenterOnScreen(".\Screenshot\\claimLoot.PNG",confidence=0.8))

