import  pyautogui,webbrowser,time,random,sys


def selectSummon(summonName):
    check = pyautogui.locateCenterOnScreen(".\Screenshot\\"+summonName+".PNG")
    if check!=None:
        pyautogui.click(check,duration=random.uniform(0.01,0.5))
    while check == None:
        pyautogui.scroll(-100)
        check = pyautogui.locateCenterOnScreen(".\Screenshot\\"+summonName+".PNG")
    pyautogui.click(check,duration=random.uniform(0.01,0.5))
def clickOK(): 
    check = pyautogui.locateCenterOnScreen(".\Screenshot\ok.PNG",confidence=0.5)
    if check!=None:
        pyautogui.click(check,duration=random.uniform(0.01,0.5))
    while check is None:
        pyautogui.scroll(-100)
        check = pyautogui.locateOnScreen(".\Screenshot\ok.PNG")
    pyautogui.click(check,duration=random.uniform(0.01,0.5))
def summonCall(summon):
    check = pyautogui.locateCenterOnScreen(".\Screenshot\summonTab.PNG")
    while check == None:
        check = pyautogui.locateCenterOnScreen(".\Screenshot\summonTab.PNG")
    time.sleep(2)
    pyautogui.click(check,duration=random.uniform(0.01,0.5))
    check = pyautogui.locateCenterOnScreen(".\Screenshot\\"+summon+"Call.PNG")
    while check == None:
        check = pyautogui.locateCenterOnScreen(".\Screenshot\\"+summon+"Call.PNG")
    pyautogui.click(check,duration=random.uniform(0.01,0.5))
    clickOK()
def attack():
    check = pyautogui.locateCenterOnScreen(".\Screenshot\\attack.PNG")
    while check is None:
        check = pyautogui.locateCenterOnScreen(".\Screenshot\\attack.PNG")
    pyautogui.click(check,duration=random.uniform(0.01,0.5))
    time.sleep(2)
def back():
    pyautogui.click(pyautogui.locateCenterOnScreen(".\Screenshot\\back.PNG"))
    time.sleep(2)
def waitForRaidEnd():
    while pyautogui.locateCenterOnScreen(".\Screenshot\end.PNG") is None:
        time.sleep(1)

#======================== Setting ==============================
#Summon to call
summon = "huanglong"
#How many run
count = 404040
#Link
fight = 'http://game.granbluefantasy.jp/#quest/supporter/400181/4'
#============================================================
i=0
while i<=count:
    sys.stdout.write("Running Round "+str(i+1)+"\n")
    while pyautogui.locateCenterOnScreen(".\Screenshot\\vee.PNG") == None:
        pyautogui.locateCenterOnScreen(".\Screenshot\\vee.PNG")
    pyautogui.click(pyautogui.locateCenterOnScreen(".\Screenshot\\vee.PNG"),duration=0.5)


    #====================== Fight Start ====================#
    selectSummon(summon)
    clickOK()
    summonCall(summon)
    back()
    attack()

    back()
    attack()
    
    back()
    waitForRaidEnd()
    webbrowser.open(fight, new=2)
    #============================= Fight END ================#


    i+=1
    sys.stdout.write("Round "+str(i)+" Finished\n")