import  pyautogui,webbrowser,time,random,sys


def selectSummon(summonName):
    shot = pyautogui.screenshot()
    check = pyautogui.locateCenterOnScreen(".\Screenshot\\"+summonName+".PNG")
    if check!=None:
        pyautogui.click(check,duration=random.uniform(0.01,0.5))
    while check == None:
        pyautogui.scroll(-100)
        shot = pyautogui.screenshot()
        check = pyautogui.locateCenterOnScreen(".\Screenshot\\"+summonName+".PNG")
    pyautogui.click(check,duration=random.uniform(0.01,0.5))
def clickOK():
    shot = pyautogui.screenshot()
    check = pyautogui.locateCenterOnScreen(".\Screenshot\ok.PNG",confidence=0.5)
    if check!=None:
        pyautogui.click(check,duration=random.uniform(0.01,0.5))
    while check is None:
        pyautogui.scroll(-100)
        shot = pyautogui.screenshot()
        check = pyautogui.locateOnScreen(".\Screenshot\ok.PNG")
    pyautogui.click(check,duration=random.uniform(0.01,0.5))
def summonCall(callSummon):
    pyautogui.screenshot()
    check = pyautogui.locateCenterOnScreen(".\Screenshot\summonTab.PNG")
    while check == None:
        pyautogui.screenshot()
        check = pyautogui.locateCenterOnScreen(".\Screenshot\summonTab.PNG")
    time.sleep(2)
    pyautogui.click(check,duration=random.uniform(0.01,0.5))
    check = pyautogui.locateCenterOnScreen(".\Screenshot\\"+callSummon+"Call.PNG")
    while check == None:
        pyautogui.screenshot()
        check = pyautogui.locateCenterOnScreen(".\Screenshot\\"+callSummon+"Call.PNG")
    pyautogui.click(check,duration=random.uniform(0.01,0.5))
    clickOK()
def attack():
    pyautogui.screenshot()
    check = pyautogui.locateCenterOnScreen(".\Screenshot\\attack.PNG")
    while check is None:
        pyautogui.screenshot()
        check = pyautogui.locateCenterOnScreen(".\Screenshot\\attack.PNG")
    pyautogui.click(check,duration=random.uniform(0.01,0.5))
#============================================================
#Summon to call
callSummon = "huanglong"
#Round
count = 40
#Link
fight = 'http://game.granbluefantasy.jp/#quest/supporter/400181/4'
#============================================================
i=0
while i<=count:
    sys.stdout.write("Running Round "+str(i+1)+"\n")
    while pyautogui.locateCenterOnScreen(".\Screenshot\\vee.PNG") == None:
        pyautogui.locateCenterOnScreen(".\Screenshot\\vee.PNG")
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
        pyautogui.screenshot()
    webbrowser.open(fight, new=2)
    i+=1
    sys.stdout.write("Round "+str(i)+" Finished\n")