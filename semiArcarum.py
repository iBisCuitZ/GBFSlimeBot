import pyautogui as auto
import webbrowser,time,random,sys,pygetwindow
def checkPot():
    if(auto.locateCenterOnScreen(".\Screenshot\\needPot.png",confidence=0.9)):
        auto.moveTo(auto.locateCenterOnScreen(".\Screenshot\\halfElixir.png",confidence=0.9))
        auto.click(auto.move(50,100))
        time.sleep(1)
        # auto.click(auto.locateCenterOnScreen(".\Screenshot\\dropdown.png",confidence=0.9))
        auto.click(auto.locateCenterOnScreen(".\Screenshot\\13.png",confidence=0.9))
        # auto.click(auto.locateCenterOnScreen(".\Screenshot\\use.png"))
        x=list( auto.locateAllOnScreen(".\Screenshot\\use.png",confidence=0.9))
        auto.click(x[1])
        clickOK()
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
        auto.click(check2,duration=random.uniform(0.01,0.2))
        return summonName2
    else : 
        auto.click(check,duration=random.uniform(0.01,0.1))
        return summonName
    clickOK()
def clickOK(): 
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
    auto.click(auto.locateCenterOnScreen(".\Screenshot\ok.PNG",confidence=0.9),duration=random.uniform(0.01,0.1))
def summonCall(summon):
    countdown=0
    check = auto.locateCenterOnScreen(".\Screenshot\summonTab.PNG")
    while check == None:
        if countdown<=5:
            check = auto.locateCenterOnScreen(".\Screenshot\summonTab.PNG")
            time.sleep(1)
            countdown+=1
        else:
            auto.click(auto.locateCenterOnScreen(".\Screenshot\\reloadBrowser.PNG",confidence=0.9))
            countdown=0    
    time.sleep(1)
    auto.click(check,duration=random.uniform(0.01,0.2))
    check = auto.locateCenterOnScreen(".\Screenshot\\"+summon+"Call.PNG")
    while check == None:
        check = auto.locateCenterOnScreen(".\Screenshot\\"+summon+"Call.PNG")
    auto.click(check,duration=random.uniform(0.01,0.2))
    clickOK()
    time.sleep(1)
def quickSummon():
    countdown=0
    check = auto.locateCenterOnScreen(".\Screenshot\\quickSummon.PNG",confidence=0.8)
    while check is None:
        if countdown<=5:
            check = auto.locateCenterOnScreen(".\Screenshot\\quickSummon.PNG",confidence=0.8)
            print("quick sum check")
            time.sleep(1)
            countdown+=1
        else:
            auto.click(auto.locateCenterOnScreen(".\Screenshot\\reloadBrowser.PNG",confidence=0.8))
            countdown=0
    auto.click(check,duration=random.uniform(0.01,0.2))
    time.sleep(2)
def quickSummonV2():
    countdown=0
    check = auto.locateCenterOnScreen(".\Screenshot\\quickSummonV2.PNG",confidence=0.9)
    while check is None:
        if countdown<=5:
            check = auto.locateCenterOnScreen(".\Screenshot\\quickSummonV2.PNG",confidence=0.9)
            time.sleep(1)
            countdown+=1
        else:
            auto.click(auto.locateCenterOnScreen(".\Screenshot\\reloadBrowser.PNG",confidence=0.9))
            countdown=0
    auto.click(check,duration=random.uniform(0.01,0.2))
    time.sleep(2)
def attack():
    countdown=0
    check = auto.locateCenterOnScreen(".\Screenshot\\attack.PNG",confidence=0.9)
    while check is None:
        if countdown<=5:
            check = auto.locateCenterOnScreen(".\Screenshot\\attack.PNG",confidence=0.9)
            time.sleep(1)
            countdown+=1
        else:
            auto.click(auto.locateCenterOnScreen(".\Screenshot\\reloadBrowser.PNG",confidence=0.9))
            countdown=0
    auto.click(check,duration=random.uniform(0.01,0.2))
    time.sleep(3)
def back():
    auto.click(auto.locateCenterOnScreen(".\Screenshot\\back.PNG",confidence=0.9))
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
    while auto.locateCenterOnScreen(".\Screenshot\\2nd.PNG",confidence=0.9) is None:
        time.sleep(0.5)
    while auto.locateCenterOnScreen(".\Screenshot\\skillInbar.PNG",confidence=0.8) is None:
        auto.click(auto.locateCenterOnScreen(".\Screenshot\\2nd.PNG",confidence=0.9))
        time.sleep(0.5)
    auto.moveTo(auto.locateCenterOnScreen(".\Screenshot\skillInBar.PNG",confidence=0.7))
    time.sleep(0.5)
    auto.click(auto.move(30,30))
    time.sleep(1)
    auto.click(auto.locateCenterOnScreen(".\Screenshot\\backButton.PNG",confidence=0.7))
    time.sleep(0.5)
def cha2Cast2():
    while auto.locateCenterOnScreen(".\Screenshot\\2nd.PNG",confidence=0.9) == None:
        time.sleep(0.5)
    time.sleep(1)
    while auto.locateCenterOnScreen(".\Screenshot\\skillInbar.PNG",confidence=0.8) is None:
        auto.click(auto.locateCenterOnScreen(".\Screenshot\\2nd.PNG",confidence=0.9))
        time.sleep(0.5)
    auto.moveTo(auto.locateCenterOnScreen(".\Screenshot\skillInBar.PNG",confidence=0.7))
    time.sleep(0.5)
    auto.click(auto.move(100,30))
    time.sleep(1)
    auto.click(auto.locateCenterOnScreen(".\Screenshot\\backButton.PNG",confidence=0.7))
    time.sleep(0.5)
def cha3Cast1():
    while auto.locateCenterOnScreen(".\Screenshot\\3rd.PNG",confidence=0.9) is None:
        time.sleep(0.5)
    while auto.locateCenterOnScreen(".\Screenshot\\skillInbar.PNG",confidence=0.8) is None:
        auto.click(auto.locateCenterOnScreen(".\Screenshot\\3rd.PNG",confidence=0.9))
        time.sleep(0.5)
    auto.moveTo(auto.locateCenterOnScreen(".\Screenshot\skillInBar.PNG",confidence=0.7))
    time.sleep(0.5)
    auto.click(auto.move(30,30))
    time.sleep(1)
    auto.click(auto.locateCenterOnScreen(".\Screenshot\\backButton.PNG",confidence=0.7))
    time.sleep(0.5)
def cha3Cast2():
    while auto.locateCenterOnScreen(".\Screenshot\\3rd.PNG",confidence=0.9) == None:
        time.sleep(0.5)
    time.sleep(1)
    while auto.locateCenterOnScreen(".\Screenshot\\skillInbar.PNG",confidence=0.8) is None:
        auto.click(auto.locateCenterOnScreen(".\Screenshot\\3rd.PNG",confidence=0.9))
        time.sleep(0.5)
    auto.moveTo(auto.locateCenterOnScreen(".\Screenshot\skillInBar.PNG",confidence=0.7))
    time.sleep(0.5)
    auto.click(auto.move(100,30))
    time.sleep(1)
    auto.click(auto.locateCenterOnScreen(".\Screenshot\\backButton.PNG",confidence=0.7))
    time.sleep(0.5)
def cha4Cast1():
    while auto.locateCenterOnScreen(".\Screenshot\\4th.png",confidence=0.9) is None:
        time.sleep(0.5)
    while auto.locateCenterOnScreen(".\Screenshot\\skillInbar.PNG",confidence=0.8) is None:
        auto.click(auto.locateCenterOnScreen(".\Screenshot\\4th.png",confidence=0.9))
        time.sleep(0.5)
    auto.moveTo(auto.locateCenterOnScreen(".\Screenshot\skillInBar.PNG",confidence=0.7))
    time.sleep(0.5)
    auto.click(auto.move(30,30))
    auto.click(auto.locateCenterOnScreen(".\Screenshot\\backButton.PNG",confidence=0.7))
    time.sleep(0.1)
def cha4Cast2():
    while auto.locateCenterOnScreen(".\Screenshot\\3rd.PNG",confidence=0.9) == None:
        time.sleep(0.5)
    time.sleep(1)
    while auto.locateCenterOnScreen(".\Screenshot\\skillInbar.PNG",confidence=0.8) is None:
        auto.click(auto.locateCenterOnScreen(".\Screenshot\\4th.PNG",confidence=0.9))
        time.sleep(0.5)
    auto.moveTo(auto.locateCenterOnScreen(".\Screenshot\skillInBar.PNG",confidence=0.7))
    time.sleep(0.5)
    auto.click(auto.move(100,30))
    time.sleep(1)
    auto.click(auto.locateCenterOnScreen(".\Screenshot\\backButton.PNG",confidence=0.7))
    time.sleep(0.5)
def cha4Cast3():
    while auto.locateCenterOnScreen(".\Screenshot\\4th.png",confidence=0.9) == None:
        time.sleep(0.5)
    time.sleep(1)
    while auto.locateCenterOnScreen(".\Screenshot\\skillInbar.PNG",confidence=0.8) is None:
        auto.click(auto.locateCenterOnScreen(".\Screenshot\\4th.png",confidence=0.9))
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
def fullAuto():
    wait=0
    while auto.locateCenterOnScreen(".\Screenshot\\attack.PNG",confidence=0.9) is None :
        print("CheckFullAutoLoop")
        time.sleep(1)
        wait+=1
        if wait>=6:
            auto.click(auto.locateCenterOnScreen(".\Screenshot\\reload.PNG",confidence=0.7))
            wait=0
    time.sleep(1)
    auto.click(auto.locateCenterOnScreen(".\Screenshot\\full.PNG",confidence=0.7))
#======================== Setting ==============================
#Summon to call
callSummon = "lucifer"
callSummon2 = "chevalier"
#How many run
count = 9999
#============================================================
i=1
while i<=count:
    win=pygetwindow.getWindowsWithTitle('Granblue Fantasy')[0]
    print(win)
    win.activate()
    sys.stdout.write("Running Round "+str(i)+"\n")
    clickOK()
    time.sleep(2)
    checkPot()
    #====================== Fight Start ====================#
    time.sleep(4)
    # cha4Cast2()
    # semiAuto()
    # cha1Cast1()
    # fullAuto()
    # cha1Cast2()
    attack()
    # time.sleep(17)
    # quickSummon()
    # cha4Cast3()
    # cha4Cast3()
    # attack()
    back()
    # cha1Cast3()
    # cha1Cast3()
    # time.sleep(6)
    # summonCall(summon)
    # time.sleep(1)
    # attack()
    # back()
    # cha4Cast3()
    # print("Attack 1")
    # back()
    # # ==== Turn 2 ====
    # attack()
    # back()
    # print("Attack 2")
    waitForRaidEnd()
    macroButton()
    #============================= Fight END ================#
    sys.stdout.write("Round "+str(i)+" Finished\n")
    sys.stdout.write("===========================\n")
    i+=1