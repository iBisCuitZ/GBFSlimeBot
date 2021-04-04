import  pyautogui,webbrowser,time,random



fight = 'http://game.granbluefantasy.jp/#quest/supporter/400151/4'

def selectSummon(summonName):
    print("in SelectSummon()")
    shot = pyautogui.screenshot()
    check = pyautogui.locateCenterOnScreen(".\Screenshot\\"+summonName+".PNG")
    if check!=None:
        pyautogui.click(check,duration=0.5)
    while check == None:
        pyautogui.scroll(-100)
        shot = pyautogui.screenshot()
        check = pyautogui.locateCenterOnScreen(".\Screenshot\\"+summonName+".PNG")
    pyautogui.click(check)

def clickOK():
    print("in Clickok()")
    i=1
    shot = pyautogui.screenshot()
    check = pyautogui.locateCenterOnScreen(".\Screenshot\ok.PNG",confidence=0.5)
    if check!=None:
        pyautogui.click(check,duration=0.2)
    while check is None:
        pyautogui.scroll(-100)
        shot = pyautogui.screenshot()
        check = pyautogui.locateOnScreen(".\Screenshot\ok.PNG")
        i+=1
    pyautogui.click(check)

def summonCall(callSummon):
    print('in SummonCall')
    pyautogui.screenshot()
    check = pyautogui.locateCenterOnScreen(".\Screenshot\summonTab.PNG")
    while check == None:
        pyautogui.screenshot()
        check = pyautogui.locateCenterOnScreen(".\Screenshot\summonTab.PNG")
    time.sleep(2)
    pyautogui.click(check)
    
    check = pyautogui.locateCenterOnScreen(".\Screenshot\\"+callSummon+"Call.PNG")
    print(check)
    while check == None:
        print('in Loop')
        pyautogui.screenshot()
        check = pyautogui.locateCenterOnScreen(".\Screenshot\\"+callSummon+"Call.PNG")
    pyautogui.click(check)
    clickOK()

def attack():
    print('in Attack')
    pyautogui.screenshot()
    check = pyautogui.locateCenterOnScreen(".\Screenshot\\attack.PNG")
    while check is None:
        pyautogui.screenshot()
        check = pyautogui.locateCenterOnScreen(".\Screenshot\\attack.PNG")
    pyautogui.click(check)

#============================================================
#Summon to call
callSummon = "huanglong"
#Round
count = 3
#============================================================
i=0
while i <= count:
    time.sleep(3)
    pyautogui.click(pyautogui.locateCenterOnScreen(".\Screenshot\\vee.PNG"),duration=0.5)
    selectSummon(callSummon)
    clickOK()
    summonCall(callSummon)
    pyautogui.click(pyautogui.locateCenterOnScreen(".\Screenshot\\back.PNG"))
    time.sleep(1)
    attack()
    time.sleep(1)
    pyautogui.click(pyautogui.locateCenterOnScreen(".\Screenshot\\back.PNG"))
    attack()
    time.sleep(2)
    pyautogui.click(pyautogui.locateCenterOnScreen(".\Screenshot\\back.PNG"))

    while pyautogui.locateCenterOnScreen(".\Screenshot\end.PNG") is None:
        print('in Check END')
        pyautogui.screenshot()
    webbrowser.open(fight, new=2)