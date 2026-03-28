import pyautogui,pygetwindow,time

def getGem():
    while pyautogui.locateCenterOnScreen(".\\test\\gem.png",confidence=0.9) is None:
        time.sleep(1)
        pyautogui.scroll(-200)
    pyautogui.click(pyautogui.locateCenterOnScreen(".\\test\\gem.png",confidence=0.9))
def skip():
    while pyautogui.locateCenterOnScreen(".\\test\\skip.png") is None:
        time.sleep(0.2)
    time.sleep(2)
    pyautogui.click(pyautogui.locateCenterOnScreen(".\\test\\skip.png"))
    while pyautogui.locateCenterOnScreen(".\\test\\skip2.png",confidence=0.9) is None:
        time.sleep(0.2)
    time.sleep(0.5)
    pyautogui.click(pyautogui.locateCenterOnScreen(".\\test\\skip2.png",confidence=0.9))
def macroButton():
    while pyautogui.locateCenterOnScreen(".\\test\\exp.png",confidence=0.9) is None:
        time.sleep(1)
    pyautogui.click(pyautogui.locateCenterOnScreen(".\\test\\macro.png"))

def clickOk():
    while pyautogui.locateCenterOnScreen(".\\test\\ok.png") is None:
        time.sleep(1)
    pyautogui.click(pyautogui.locateCenterOnScreen(".\\test\\ok.png"))

def clickOkEvent():
    while pyautogui.locateCenterOnScreen(".\\test\\okEvent.png",confidence=0.9) is None:
        time.sleep(1)
    pyautogui.click(pyautogui.locateCenterOnScreen(".\\test\\okEvent.png",confidence=0.9))


k=None
while k is None:
    print("click")
    # pyautogui.click(pyautogui.locateCenterOnScreen(".\\test\\vee.PNG"))
    time.sleep(0.5)
    pyautogui.scroll(-200)
    # getGem()
    clickOkEvent()
    skip()
    # macroButton()
    time.sleep(2)