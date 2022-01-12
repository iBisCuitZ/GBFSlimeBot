import pyautogui,pygetwindow,time

def getGem():
    while pyautogui.locateCenterOnScreen(".\\test\\gem.png") is None:
        time.sleep(1)
        pyautogui.scroll(-200)
    pyautogui.click(pyautogui.locateCenterOnScreen(".\\test\\gem.png"))
def skip():
    while pyautogui.locateCenterOnScreen(".\\test\\skip.png") is None:
        time.sleep(1)
    time.sleep(0.8)
    pyautogui.click(pyautogui.locateCenterOnScreen(".\\test\\skip.png"))
    while pyautogui.locateCenterOnScreen(".\\test\\ok.png") is None:
        time.sleep(1)
    time.sleep(0.5)
    pyautogui.click(pyautogui.locateCenterOnScreen(".\\test\\ok.png"))
def macroButton():
    while pyautogui.locateCenterOnScreen(".\\test\\exp.png") is None:
        time.sleep(1)
    pyautogui.click(pyautogui.locateCenterOnScreen(".\\test\\macro.png"))

k=None
while k is None:
    print("click")
    pyautogui.click(pyautogui.locateCenterOnScreen(".\\test\\vee.PNG"))
    time.sleep(0.5)
    pyautogui.scroll(-200)
    getGem()
    skip()
    macroButton()
    time.sleep(2)