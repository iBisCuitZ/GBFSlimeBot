import  pyautogui,webbrowser,time,random,sys,pyperclip

def attack():
    pyautogui.screenshot()
    check = pyautogui.locateCenterOnScreen(".\Screenshot\\attack.PNG")
    while check is None:
        pyautogui.screenshot()
        check = pyautogui.locateCenterOnScreen(".\Screenshot\\attack.PNG")
    pyautogui.click(check,duration=random.uniform(0.01,0.5))
def selectSummon(summonName):
    print('in Select Summon')
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
def getReward():
    print("in get reward")
    pyautogui.click(pyautogui.locateCenterOnScreen(".\Screenshot\check.PNG"))
    time.sleep(2)
    pyautogui.moveTo(pyautogui.locateCenterOnScreen(".\Screenshot\pending.PNG"))
    pyautogui.click(pyautogui.move(0,50))
    time.sleep(2)
    pyautogui.hotkey('alt','left')
    pyautogui.hotkey('alt','left')
#========= Option =========#
callSummon = "kaguya"
run=30
i=0
joined =0
while i!=run:
    if pyautogui.locateCenterOnScreen(".\Screenshot\check.PNG") != None:
        getReward()
    elif joined != 3:
        #===========RaidFinder========#
        pyautogui.moveTo(pyautogui.locateCenterOnScreen(".\Screenshot\moreOptionIcon.PNG"))
        print("1")
        pyautogui.click(pyautogui.move(0,80))
        time.sleep(0.5)
        #========GameClients==========#
        print('click Vee')
        pyautogui.click(pyautogui.locateCenterOnScreen(".\Screenshot\\vee.PNG"))
        pyautogui.click(pyautogui.locateCenterOnScreen(".\Screenshot\enterID.PNG"))
        pyautogui.moveTo(pyautogui.locateCenterOnScreen(".\Screenshot\joinARoom.PNG"))
        pyautogui.click(pyautogui.move(-250,0))
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)
        print('click join')
        if pyautogui.locateCenterOnScreen(".\Screenshot\dupeRaid.PNG") == None :
            if pyautogui.locateCenterOnScreen(".\Screenshot\ended.PNG") == None:
                pyautogui.click(pyautogui.locateCenterOnScreen(".\Screenshot\joinARoom.PNG"))
                pyautogui.click(pyautogui.locateCenterOnScreen(".\Screenshot\joinARoom.PNG"))
                time.sleep(1)
                #=====SelectSummon=====#
                selectSummon(callSummon)
                clickOK()
                #===== Timeline =====#
                attack()
                pyautogui.hotkey('alt','left')
                pyautogui.hotkey('alt','left')
                time.sleep(1)
                pyautogui.scroll(-100)
                joined = len(list(pyautogui.locateAllOnScreen(".\Screenshot\joined.PNG")))
        else:
            pyautogui.hotkey('f5')
    else:
        while joined == 3:
            time.sleep(5)
            pyautogui.hotkey('f5')
            time.sleep(1)
            pyautogui.scroll(-100)
            joined = len(list(pyautogui.locateAllOnScreen(".\Screenshot\joined.PNG")))
    i+=1
    