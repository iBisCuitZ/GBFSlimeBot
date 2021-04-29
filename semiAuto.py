import pyautogui as auto
import webbrowser,time,random,sys,pygetwindow

def macroButton():
    auto.click(auto.locateCenterOnScreen(".\Screenshot\\macroButton.png",confidence=0.9))
def selectSummon(summonName):
    check = auto.locateCenterOnScreen(".\Screenshot\\"+summonName+".PNG")
    print("in selectSummon()")
    if check!=None:
        auto.click(check,duration=random.uniform(0.01,0.5))
    while check == None:
        auto.scroll(-100)
        check = auto.locateCenterOnScreen(".\Screenshot\\"+summonName+".PNG")
    auto.click(check,duration=random.uniform(0.01,0.5))
def clickOK(): 
    print("in click OK")
    check = auto.locateCenterOnScreen(".\Screenshot\ok.PNG",confidence=0.5)
    if check != None:
        print("found")
        auto.click(check,duration=random.uniform(0.01,0.5))
        return
    while check is None:
        print("not found")
        auto.scroll(-100)
        check = auto.locateOnScreen(".\Screenshot\ok.PNG",confidence=0.5)
    auto.click(check,duration=random.uniform(0.01,0.5))
def summonCall(summon):
    check = auto.locateCenterOnScreen(".\Screenshot\summonTab.PNG")
    while check == None:
        check = auto.locateCenterOnScreen(".\Screenshot\summonTab.PNG")
    time.sleep(2)
    auto.click(check,duration=random.uniform(0.01,0.5))
    check = auto.locateCenterOnScreen(".\Screenshot\\"+summon+"Call.PNG")
    while check == None:
        check = auto.locateCenterOnScreen(".\Screenshot\\"+summon+"Call.PNG")
    auto.click(check,duration=random.uniform(0.01,0.5))
    clickOK()
def attack():
    check = auto.locateCenterOnScreen(".\Screenshot\\attack.PNG")
    while check is None:
        check = auto.locateCenterOnScreen(".\Screenshot\\attack.PNG")
    auto.click(check,duration=random.uniform(0.01,0.5))
    time.sleep(2)
def back():
    auto.click(auto.locateCenterOnScreen(".\Screenshot\\back.PNG"))
    time.sleep(2)
def waitForRaidEnd():
    while auto.locateCenterOnScreen(".\Screenshot\end.PNG",confidence=0.7) is None:
        time.sleep(1)
def cha1Cast1():
    while auto.locateCenterOnScreen(".\Screenshot\\1st.PNG",confidence=0.7) is None:
        time.sleep(0.5)
    while auto.locateCenterOnScreen(".\Screenshot\\skillInbar.PNG",confidence=0.8) is None:
        auto.click(auto.locateCenterOnScreen(".\Screenshot\\1st.PNG",confidence=0.7))
        time.sleep(0.5)
    auto.moveTo(auto.locateCenterOnScreen(".\Screenshot\skillInBar.PNG",confidence=0.7))
    time.sleep(0.5)
    auto.click(auto.move(30,30))
    auto.click(auto.locateCenterOnScreen(".\Screenshot\\backButton.PNG",confidence=0.7))
    time.sleep(0.1)
def cha1Cast2():
    while auto.locateCenterOnScreen(".\Screenshot\\1st.PNG",confidence=0.7) == None:
        time.sleep(0.5)
    time.sleep(1)
    while auto.locateCenterOnScreen(".\Screenshot\\skillInbar.PNG",confidence=0.8) is None:
        auto.click(auto.locateCenterOnScreen(".\Screenshot\\1st.PNG",confidence=0.7))
        time.sleep(0.5)
    auto.moveTo(auto.locateCenterOnScreen(".\Screenshot\skillInBar.PNG",confidence=0.7))
    time.sleep(0.5)
    auto.click(auto.move(100,30))
    time.sleep(1)
    auto.click(auto.locateCenterOnScreen(".\Screenshot\\backButton.PNG",confidence=0.7))
    time.sleep(0.5)
def cha1Cast3():
    while auto.locateCenterOnScreen(".\Screenshot\\1st.PNG",confidence=0.7) == None:
        time.sleep(0.5)
    time.sleep(1)
    while auto.locateCenterOnScreen(".\Screenshot\\skillInbar.PNG",confidence=0.8) is None:
        auto.click(auto.locateCenterOnScreen(".\Screenshot\\1st.PNG",confidence=0.7))
        time.sleep(0.5)
    auto.moveTo(auto.locateCenterOnScreen(".\Screenshot\skillInBar.PNG",confidence=0.7))
    time.sleep(0.5)
    auto.click(auto.move(180,30))
    time.sleep(1)
    auto.click(auto.locateCenterOnScreen(".\Screenshot\\backButton.PNG",confidence=0.7))
    time.sleep(0.5)
def cha1Cast4():
    while auto.locateCenterOnScreen(".\Screenshot\\1st.PNG",confidence=0.7) == None:
        time.sleep(0.5)
    time.sleep(1)
    while auto.locateCenterOnScreen(".\Screenshot\\skillInbar.PNG",confidence=0.8) is None:
        auto.click(auto.locateCenterOnScreen(".\Screenshot\\1st.PNG",confidence=0.7))
        time.sleep(0.5)
    auto.moveTo(auto.locateCenterOnScreen(".\Screenshot\skillInBar.PNG",confidence=0.7))
    time.sleep(0.5)
    auto.click(auto.move(270,30))
    time.sleep(1)
    auto.click(auto.locateCenterOnScreen(".\Screenshot\\backButton.PNG",confidence=0.7))
    time.sleep(0.5)
def cha2Cast1():
    while auto.locateCenterOnScreen(".\Screenshot\\2nd.PNG",confidence=0.7) is None:
        time.sleep(0.5)
    while auto.locateCenterOnScreen(".\Screenshot\\skillInbar.PNG",confidence=0.8) is None:
        auto.click(auto.locateCenterOnScreen(".\Screenshot\\2nd.PNG",confidence=0.7))
        time.sleep(0.5)
    auto.moveTo(auto.locateCenterOnScreen(".\Screenshot\skillInBar.PNG",confidence=0.7))
    time.sleep(0.5)
    auto.click(auto.move(30,30))
    time.sleep(1)
    auto.click(auto.locateCenterOnScreen(".\Screenshot\\backButton.PNG",confidence=0.7))
    time.sleep(0.5)
def cha3Cast1():
    while auto.locateCenterOnScreen(".\Screenshot\\3rd.PNG",confidence=0.7) is None:
        time.sleep(0.5)
    while auto.locateCenterOnScreen(".\Screenshot\\skillInbar.PNG",confidence=0.8) is None:
        auto.click(auto.locateCenterOnScreen(".\Screenshot\\3rd.PNG",confidence=0.7))
        time.sleep(0.5)
    auto.moveTo(auto.locateCenterOnScreen(".\Screenshot\skillInBar.PNG",confidence=0.7))
    time.sleep(0.5)
    auto.click(auto.move(30,30))
    time.sleep(1)
    auto.click(auto.locateCenterOnScreen(".\Screenshot\\backButton.PNG",confidence=0.7))
    time.sleep(0.5)
def cha3Cast2():
    while auto.locateCenterOnScreen(".\Screenshot\\3rd.PNG",confidence=0.7) == None:
        time.sleep(0.5)
    time.sleep(1)
    while auto.locateCenterOnScreen(".\Screenshot\\skillInbar.PNG",confidence=0.8) is None:
        auto.click(auto.locateCenterOnScreen(".\Screenshot\\3rd.PNG",confidence=0.7))
        time.sleep(0.5)
    auto.moveTo(auto.locateCenterOnScreen(".\Screenshot\skillInBar.PNG",confidence=0.7))
    time.sleep(0.5)
    auto.click(auto.move(100,30))
    time.sleep(1)
    auto.click(auto.locateCenterOnScreen(".\Screenshot\\backButton.PNG",confidence=0.7))
    time.sleep(0.5)
def semiAuto():
    while auto.locateCenterOnScreen(".\Screenshot\\attack.PNG") is None:
        time.sleep(1)
    time.sleep(3)
    auto.click(auto.locateCenterOnScreen(".\Screenshot\\attack.PNG",confidence=0.7))
    time.sleep(1.5)
    auto.click(auto.locateCenterOnScreen(".\Screenshot\\semi.PNG",confidence=0.7))
#======================== Setting ==============================
#Summon to call
summon = "huanglong"
summon2 = "agni"
#How many run
count = 404040
#Link
fight = 'http://game.granbluefantasy.jp/#quest/supporter/510031/5'
#============================================================
i=0
while i<=count:
    win=pygetwindow.getWindowsWithTitle('Granblue Fantasy')[0]
    win.activate()
    sys.stdout.write("Running Round "+str(i+1)+"\n")
    while auto.locateCenterOnScreen(".\Screenshot\\vee.PNG") is None:
        auto.locateCenterOnScreen(".\Screenshot\\vee.PNG")
    auto.click(auto.locateCenterOnScreen(".\Screenshot\\vee.PNG"),duration=0.5)
    selectSummon(summon)
    clickOK()
    #====================== Fight Start ====================#
    # summonCall(summon)
    time.sleep(3)
    if auto.locateCenterOnScreen(".\Screenshot\\pickedUp.PNG",confidence=0.7) != None:
        print("in if picked up")
        clickOK()
    # cha1Cast1()
    semiAuto()
    # time.sleep(1)
    # cha1Cast2()
    # cha1Cast3()
    # cha3Cast1()
    # attack()
    # back()
    waitForRaidEnd()
    macroButton()
    #============================= Fight END ================#


    i+=1
    sys.stdout.write("Round "+str(i)+" Finished\n")