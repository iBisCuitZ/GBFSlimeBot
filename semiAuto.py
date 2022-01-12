import pyautogui as auto
import webbrowser,time,random,sys,pygetwindow

def macroButton():
    auto.click(auto.locateCenterOnScreen(".\Screenshot\\macroButton.png",confidence=0.9))
def eventButton():
    auto.click(auto.locateCenterOnScreen(".\Screenshot\\event.png",confidence=0.9))    
def selectSummon(summonName,summonName2):
    print('in Select Summon')
    check = auto.locateCenterOnScreen(".\Screenshot\\"+summonName+".PNG",confidence=0.9)
    check2 = auto.locateCenterOnScreen(".\Screenshot\\"+summonName2+".PNG",confidence=0.9)
    time.sleep(2)
    while check == None and check2 == None:
        auto.scroll(-100)
        check = auto.locateCenterOnScreen(".\Screenshot\\"+summonName+".PNG",confidence=0.9)
        check2 = auto.locateCenterOnScreen(".\Screenshot\\"+summonName2+".PNG",confidence=0.9)
    if check == None:
        auto.click(check2,duration=random.uniform(0.01,0.5))
        return summonName2
    else : 
        auto.click(check,duration=random.uniform(0.01,0.5))
        return summonName
    clickOK()
def clickOK(): 
    print("in click OK")
    auto.locateCenterOnScreen(".\Screenshot\ok.PNG",confidence=0.9)
    if auto.locateCenterOnScreen(".\Screenshot\ok.PNG",confidence=0.9) != None:
        print("found")
        time.sleep(1)
        auto.click(auto.locateCenterOnScreen(".\Screenshot\ok.PNG",confidence=0.9))
        return
    while auto.locateCenterOnScreen(".\Screenshot\ok.PNG",confidence=0.9) is None:
        print("not found")
        auto.scroll(-200)
        time.sleep(1)
    print("XD")
    auto.click(auto.locateCenterOnScreen(".\Screenshot\ok.PNG",confidence=0.9),duration=random.uniform(0.01,0.5))
def summonCall(summon):
    check = auto.locateCenterOnScreen(".\Screenshot\summonTab.PNG")
    while check == None:
        check = auto.locateCenterOnScreen(".\Screenshot\summonTab.PNG")
    time.sleep(1)
    auto.click(check,duration=random.uniform(0.01,0.5))
    check = auto.locateCenterOnScreen(".\Screenshot\\"+summon+"Call.PNG")
    while check == None:
        check = auto.locateCenterOnScreen(".\Screenshot\\"+summon+"Call.PNG")
    auto.click(check,duration=random.uniform(0.01,0.5))
    clickOK()
    time.sleep(1)
def attack():
    check = auto.locateCenterOnScreen(".\Screenshot\\attack.PNG",confidence=0.9)
    while check is None:
        check = auto.locateCenterOnScreen(".\Screenshot\\attack.PNG",confidence=0.9)
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
    auto.click(auto.move(120,30))
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
def cha4Cast1():
    while auto.locateCenterOnScreen(".\Screenshot\\4th.png",confidence=0.7) is None:
        time.sleep(0.5)
    while auto.locateCenterOnScreen(".\Screenshot\\skillInbar.PNG",confidence=0.8) is None:
        auto.click(auto.locateCenterOnScreen(".\Screenshot\\4th.png",confidence=0.7))
        time.sleep(0.5)
    auto.moveTo(auto.locateCenterOnScreen(".\Screenshot\skillInBar.PNG",confidence=0.7))
    time.sleep(0.5)
    auto.click(auto.move(30,30))
    auto.click(auto.locateCenterOnScreen(".\Screenshot\\backButton.PNG",confidence=0.7))
    time.sleep(0.1)
def cha4Cast3():
    while auto.locateCenterOnScreen(".\Screenshot\\4th.png",confidence=0.7) == None:
        time.sleep(0.5)
    time.sleep(1)
    while auto.locateCenterOnScreen(".\Screenshot\\skillInbar.PNG",confidence=0.8) is None:
        auto.click(auto.locateCenterOnScreen(".\Screenshot\\4th.png",confidence=0.7))
        time.sleep(0.5)
    auto.moveTo(auto.locateCenterOnScreen(".\Screenshot\skillInBar.PNG",confidence=0.7))
    time.sleep(0.5)
    auto.click(auto.move(180,30))
    time.sleep(1)
    auto.click(auto.locateCenterOnScreen(".\Screenshot\\backButton.PNG",confidence=0.7))
    time.sleep(0.5)
def semiAuto():
    wait=0
    while auto.locateCenterOnScreen(".\Screenshot\\attack.PNG") is None :
        print("checksemi-attackloop")
        time.sleep(1)
        wait+=1
        if wait>=6:
            auto.click(auto.locateCenterOnScreen(".\Screenshot\\reload.PNG",confidence=0.7))        
    time.sleep(3)
    auto.click(auto.locateCenterOnScreen(".\Screenshot\\attack.PNG",confidence=0.7))
    time.sleep(1.5)
    auto.click(auto.locateCenterOnScreen(".\Screenshot\\semi.PNG",confidence=0.7))
#======================== Setting ==============================
#Summon to call
callSummon = "grimnir"
callSummon2 = "zephyrus"
#How many run
count = 700000000000
#Link
fight = 'http://game.granbluefantasy.jp/#quest/supporter/779061/1'
#============================================================
i=0
while i<=count:
    win=pygetwindow.getWindowsWithTitle('Granblue Fantasy')[0]
    win.activate()
    sys.stdout.write("Running Round "+str(i+1)+"\n")
    while auto.locateCenterOnScreen(".\Screenshot\\vee.PNG") is None:
        auto.locateCenterOnScreen(".\Screenshot\\vee.PNG")
    auto.click(auto.locateCenterOnScreen(".\Screenshot\\vee.PNG"),duration=0.5)
    summon=selectSummon(callSummon,callSummon2)
    print("Found Summon")
    clickOK()
    time.sleep(3)
    #====================== Fight Start ====================#
    time.sleep(3)
    if auto.locateCenterOnScreen(".\Screenshot\\pickedUp.PNG",confidence=0.7) != None:
        print("in if picked up")
        clickOK()
    
    # cha3Cast2()
    # semiAuto()
    cha1Cast1()
    cha1Cast2()
    # cha1Cast3()
    # cha1Cast3()
    # cha3Cast1()
    # time.sleep(6)
    # cha4Cast1()
    # summonCall(summon)
    # time.sleep(1)
    # back()
    # # cha4Cast3()
    # attack()
    # print("Attack 1")
    # back()
    # # ==== Turn 2 ====
    attack()
    back()
    # print("Attack 2")
    waitForRaidEnd()
    eventButton()
    auto.move(0,100)
    time.sleep(2)
    auto.scroll(-300)
    if auto.locateCenterOnScreen(".\Screenshot\\nmEvent.PNG",confidence=0.7) != None:
        auto.click(auto.locateCenterOnScreen(".\Screenshot\\nmEvent.PNG",confidence=0.7))
        time.sleep(0.5)
        auto.click(auto.locateCenterOnScreen(".\Screenshot\\claimLoot.PNG",confidence=0.9))
        waitForRaidEnd()
    macroButton()
    #============================= Fight END ================#


    i+=1
    sys.stdout.write("Round "+str(i)+" Finished\n")