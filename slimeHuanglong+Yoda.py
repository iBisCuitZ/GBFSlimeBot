import pyautogui as auto
import webbrowser,time,random,sys,pygetwindow

def macroButton():
    auto.click(auto.locateCenterOnScreen(".\Screenshot\\macroButton.png",confidence=0.9))
def selectSummon(summonName):
    check = auto.locateCenterOnScreen(".\Screenshot\\"+summonName+".PNG")
    print("in selectSummon()")
    if check!=None:
        auto.click(check,duration=random.uniform(0.01,0.5))
    else:
        while check == None:
            auto.scroll(-200)
            time.sleep(2)
            check = auto.locateCenterOnScreen(".\Screenshot\\"+summonName+".PNG",confidence=0.8)
    auto.click(check,duration=random.uniform(0.01,0.5))
    auto.click(check)
def clickOK(): 
    check = auto.locateCenterOnScreen(".\Screenshot\ok.PNG",confidence=0.8)
    if check!=None:
        auto.click(check,duration=random.uniform(0.01,0.5))
    while check is None:
        auto.scroll(-100)
        time.sleep(0.2)
        check = auto.locateOnScreen(".\Screenshot\ok.PNG",confidence=0.8)
    auto.click(check,duration=random.uniform(0.01,0.5))
def summonCall(summon):
    check = auto.locateCenterOnScreen(".\Screenshot\summonTab.PNG",confidence=0.8)
    while check == None:
        check = auto.locateCenterOnScreen(".\Screenshot\summonTab.PNG",confidence=0.8)
    time.sleep(2)
    auto.click(check,duration=random.uniform(0.01,0.5))
    check = auto.locateCenterOnScreen(".\Screenshot\\"+summon+"Call.PNG",confidence=0.8)
    while check == None:
        check = auto.locateCenterOnScreen(".\Screenshot\\"+summon+"Call.PNG",confidence=0.8)
    auto.click(check,duration=random.uniform(0.01,0.5))
    clickOK()
def attack():
    check = auto.locateCenterOnScreen(".\Screenshot\\attack.PNG",confidence=0.9)
    while check is None:
        print("check attack")
        check = auto.locateCenterOnScreen(".\Screenshot\\attack.PNG",confidence=0.9)
    auto.click(check,duration=random.uniform(0.01,0.5))
    time.sleep(2)
def back():
    print("press back")
    auto.click(auto.locateCenterOnScreen(".\Screenshot\\back.PNG",confidence=0.8))
    time.sleep(2)
def waitForRaidEnd():
    while auto.locateCenterOnScreen(".\Screenshot\end.PNG",confidence=0.8) is None:
        time.sleep(1)
        print("waiting to end")
def cha1Cast1():
    print("1start")
    while auto.locateCenterOnScreen(".\Screenshot\\1st.PNG",confidence=0.7) == None:
        time.sleep(0.5)
    time.sleep(1)
    auto.click(auto.locateCenterOnScreen(".\Screenshot\\1st.PNG",confidence=0.7))
    time.sleep(0.5)
    auto.moveTo(auto.locateCenterOnScreen(".\Screenshot\skillInBar.PNG",confidence=0.7))
    auto.click(auto.move(30,30))
    time.sleep(0.5)
    auto.click(auto.locateCenterOnScreen(".\Screenshot\\backButton.PNG"))
    time.sleep(0.5)
    print("1end")
def cha1Cast2():
    print("12start")
    while auto.locateCenterOnScreen(".\Screenshot\\1st.PNG",confidence=0.7) == None:
        time.sleep(0.5)
    time.sleep(1)
    auto.click(auto.locateCenterOnScreen(".\Screenshot\\1st.PNG",confidence=0.7))
    time.sleep(0.5)
    auto.moveTo(auto.locateCenterOnScreen(".\Screenshot\skillInBar.PNG",confidence=0.7))
    auto.click(auto.move(100,30))
    time.sleep(0.5)
    auto.click(auto.locateCenterOnScreen(".\Screenshot\\backButton.PNG"))
    time.sleep(0.5)
    print("12end")
def cha1Cast3():
    print("13start")
    while auto.locateCenterOnScreen(".\Screenshot\\1st.PNG",confidence=0.7) == None:
        time.sleep(0.5)
    time.sleep(1)
    auto.click(auto.locateCenterOnScreen(".\Screenshot\\1st.PNG",confidence=0.7))
    time.sleep(0.5)
    auto.moveTo(auto.locateCenterOnScreen(".\Screenshot\skillInBar.PNG",confidence=0.7))
    auto.click(auto.move(180,30))
    time.sleep(0.5)
    auto.click(auto.locateCenterOnScreen(".\Screenshot\\backButton.PNG",confidence=0.9))
    time.sleep(0.5)
    print("13end")
def cha1Cast4():
    while auto.locateCenterOnScreen(".\Screenshot\\1st.PNG",confidence=0.7) == None:
        time.sleep(0.5)
    time.sleep(1)
    auto.click(auto.locateCenterOnScreen(".\Screenshot\\1st.PNG",confidence=0.7))
    time.sleep(0.5)
    auto.moveTo(auto.locateCenterOnScreen(".\Screenshot\skillInBar.PNG",confidence=0.7))
    auto.click(auto.move(270,30))
    time.sleep(0.5)
    auto.click(auto.locateCenterOnScreen(".\Screenshot\\backButton.PNG"))
    time.sleep(0.5)
def cha2Cast1():
    print("21start")
    while auto.locateCenterOnScreen(".\Screenshot\\2nd.PNG",confidence=0.7) is None:
        time.sleep(0.5)
    while auto.locateCenterOnScreen(".\Screenshot\\skillInbar.PNG",confidence=0.8) is None:
        auto.click(auto.locateCenterOnScreen(".\Screenshot\\2nd.PNG",confidence=0.7))
        time.sleep(0.5)
    auto.moveTo(auto.locateCenterOnScreen(".\Screenshot\skillInBar.PNG",confidence=0.7))
    auto.click(auto.move(30,30))
    time.sleep(0.5)
    while auto.locateCenterOnScreen(".\Screenshot\\backButton.PNG",confidence=0.7) != None:
        auto.click(auto.locateCenterOnScreen(".\Screenshot\\backButton.PNG",confidence=0.7))
    time.sleep(0.5)
    print("21end")
def cha3Cast1():
    print("31start")
    while auto.locateCenterOnScreen(".\Screenshot\\3rd.PNG",confidence=0.7) is None:
        time.sleep(0.5)
    while auto.locateCenterOnScreen(".\Screenshot\\skillInbar.PNG",confidence=0.8) is None:
        auto.click(auto.locateCenterOnScreen(".\Screenshot\\3rd.PNG",confidence=0.7))
        time.sleep(0.5)
    auto.moveTo(auto.locateCenterOnScreen(".\Screenshot\skillInBar.PNG",confidence=0.7))
    auto.click(auto.move(30,30))
    time.sleep(0.5)
    auto.click(auto.locateCenterOnScreen(".\Screenshot\\backButton.PNG"))
    time.sleep(0.5)
    print("31end")
def cha3Cast2():
    print("32start")
    while auto.locateCenterOnScreen(".\Screenshot\\3rd.PNG",confidence=0.7) == None:
        time.sleep(0.5)
    time.sleep(1)
    while auto.locateCenterOnScreen(".\Screenshot\\skillInbar.PNG",confidence=0.8) is None:
        auto.click(auto.locateCenterOnScreen(".\Screenshot\\3rd.PNG",confidence=0.7))
        time.sleep(0.5)
    auto.moveTo(auto.locateCenterOnScreen(".\Screenshot\skillInBar.PNG",confidence=0.7))
    auto.click(auto.move(100,30))
    time.sleep(0.5)
    auto.click(auto.locateCenterOnScreen(".\Screenshot\\backButton.PNG",confidence=0.7))
    time.sleep(0.5)
    print("32end")
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
    win=pygetwindow.getWindowsWithTitle('Granblue Fantasy')[0]
    win.activate()
    while auto.locateCenterOnScreen(".\Screenshot\\vee.PNG",confidence=0.8) == None:
        auto.locateCenterOnScreen(".\Screenshot\\vee.PNG",confidence=0.8)
    auto.click(auto.locateCenterOnScreen(".\Screenshot\\vee.PNG",confidence=0.8),clicks=2)
    selectSummon(summon)
    clickOK()
    #====================== Fight Start ====================#
    # summonCall(summon)
    time.sleep(5)
    summonCall(summon)
    back()
    print("attack1 start")
    attack()
    print("attack1 end")
    back()
    print("attack2 start")
    attack()
    time.sleep(3)
    print("attack2 end")
    back()
    print("waitend")
    waitForRaidEnd()
    macroButton()
    #============================= Fight END ================#
    i+=1
    sys.stdout.write("Round "+str(i)+" Finished\n")