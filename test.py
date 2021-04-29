import pyautogui,pygetwindow

win=pygetwindow.getWindowsWithTitle('New Tab')[0]
win.activate()
pyautogui.click(pyautogui.locateCenterOnScreen(".\\test\\yt.PNG"))
pyautogui.click(pyautogui.locateCenterOnScreen(".\\test\\yt.PNG"))