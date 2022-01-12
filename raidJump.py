import  webbrowser,time,random,sys,pyperclip,pygetwindow
import pyautogui as auto
import keyboard
def attack():
    auto.screenshot()
    check = auto.locateCenterOnScreen(".\Screenshot\\attack.PNG")
    while check is None:
        check = auto.locateCenterOnScreen(".\Screenshot\\attack.PNG")
    auto.click(check,duration=random.uniform(0.01,0.5))
    time.sleep(1.5)
def selectSummon(summonName,summonName2):
    print('in Select Summon')
    check = auto.locateCenterOnScreen(".\Screenshot\\"+summonName+".PNG",confidence=0.9)
    check2 = auto.locateCenterOnScreen(".\Screenshot\\"+summonName2+".PNG",confidence=0.9)
    time.sleep(2)
    while check is None and check2 is None:
        auto.scroll(-100)
        check = auto.locateCenterOnScreen(".\Screenshot\\"+summonName+".PNG",confidence=0.9)
        check2 = auto.locateCenterOnScreen(".\Screenshot\\"+summonName2+".PNG",confidence=0.9)
    if check == None:
        auto.click(check2,duration=random.uniform(0.01,0.5))
    else : 
        auto.click(check,duration=random.uniform(0.01,0.5))
    
    clickOK()
def clickOK():
    auto.locateCenterOnScreen(".\Screenshot\ok.PNG",confidence=0.9)
    if auto.locateCenterOnScreen(".\Screenshot\ok.PNG",confidence=0.9)!=None:
        auto.click(auto.locateCenterOnScreen(".\Screenshot\ok.PNG",confidence=0.9),duration=random.uniform(0.01,0.5))
    while auto.locateCenterOnScreen(".\Screenshot\ok.PNG",confidence=0.9) is None:
        auto.scroll(-100)
        time.sleep(1)
    auto.click(auto.locateCenterOnScreen(".\Screenshot\ok.PNG",confidence=0.9),duration=random.uniform(0.01,0.5))
    time.sleep(3)
def getReward():
    auto.click(auto.locateCenterOnScreen(".\Screenshot\check.PNG",confidence=0.8))
    time.sleep(2)
    auto.moveTo(auto.locateCenterOnScreen(".\Screenshot\pending.PNG"))
    auto.click(auto.move(0,50))
    time.sleep(2)
    auto.hotkey('alt','left')
    auto.hotkey('alt','left')
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
    while auto.locateCenterOnScreen(".\Screenshot\\1st.PNG",confidence=0.7) is None:
        time.sleep(0.5)
    while auto.locateCenterOnScreen(".\Screenshot\\skillInbar.PNG",confidence=0.8) is None:
        auto.click(auto.locateCenterOnScreen(".\Screenshot\\1st.PNG",confidence=0.7))
        time.sleep(0.5)
    auto.moveTo(auto.locateCenterOnScreen(".\Screenshot\skillInBar.PNG",confidence=0.7))
    time.sleep(0.5)
    auto.click(auto.move(120,30))
    auto.click(auto.locateCenterOnScreen(".\Screenshot\\backButton.PNG",confidence=0.7))
    time.sleep(0.1)
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
def cha3Cast3():
    while auto.locateCenterOnScreen(".\Screenshot\\3rd.PNG",confidence=0.7) == None:
        time.sleep(0.5)
    time.sleep(1)
    while auto.locateCenterOnScreen(".\Screenshot\\skillInbar.PNG",confidence=0.8) is None:
        auto.click(auto.locateCenterOnScreen(".\Screenshot\\3rd.PNG",confidence=0.7))
        time.sleep(0.5)
    auto.moveTo(auto.locateCenterOnScreen(".\Screenshot\skillInBar.PNG",confidence=0.7))
    time.sleep(0.5)
    auto.click(auto.move(180,30))
    time.sleep(1)
    auto.click(auto.locateCenterOnScreen(".\Screenshot\\backButton.PNG",confidence=0.7))
    time.sleep(0.5)
def back():
    auto.click(auto.locateCenterOnScreen(".\Screenshot\\back.PNG"))
    time.sleep(2)
def reload():
    auto.click(auto.locateCenterOnScreen(".\Screenshot\\reload.PNG"))
    time.sleep(2)
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
#========= Option =========#
callSummon = "zephyrus"
callSummon2 = "grimnir"
run=300000
i=0
joined =0
while i!=run:
    if auto.locateCenterOnScreen(".\Screenshot\check.PNG") != None:
        while auto.locateCenterOnScreen(".\Screenshot\check.PNG") != None:
            getReward()
            auto.locateCenterOnScreen(".\Screenshot\check.PNG")
            time.sleep(1)
    elif joined != 3:
        #===========RaidFinder========#
        win=pygetwindow.getWindowsWithTitle('Granblue Raid Finder')[0]
        win.activate()
        auto.moveTo(auto.locateCenterOnScreen(".\Screenshot\\moreOptionIcon.PNG",confidence=0.8))
        time.sleep(0.5)
        auto.click(auto.move(0,70))
        time.sleep(0.5)
        print('move fin')
        #========GameClients==========#
        print("click enterID")
        auto.click(auto.locateCenterOnScreen(".\Screenshot\\enterID.PNG",confidence=0.9))
        time.sleep(1)
        print("click Join a room")
        auto.moveTo(auto.locateCenterOnScreen(".\Screenshot\\joinARoom.PNG",confidence=0.7))
        print("move down")
        auto.click(auto.move(-240,0))
        time.sleep(1)
        print("pasted")
        # auto.hotkey('ctrl','v')
        keyboard.press_and_release('ctrl+v')
        time.sleep(1)
        print('click join')
        auto.click(auto.locateCenterOnScreen(".\Screenshot\\joinARoom.PNG",confidence=0.7))
        time.sleep(1)
        print(auto.locateCenterOnScreen(".\Screenshot\\joinARoom.PNG",confidence=0.7))
        if auto.locateCenterOnScreen(".\Screenshot\\raidNoti.PNG",confidence=0.8) == None and auto.locateCenterOnScreen(".\Screenshot\\battleNoti.PNG",confidence=0.8) == None:
            print("Joinning")
            time.sleep(1)
            #=====SelectSummon=====#
            selectSummon(callSummon,callSummon2)
            time.sleep(0.5)
            time.sleep(3)
            if auto.locateCenterOnScreen(".\Screenshot\\raidNoti.PNG",confidence=0.8) == None and auto.locateCenterOnScreen(".\Screenshot\\battleNoti.PNG",confidence=0.8) == None:
                #===== Timeline =====#
                print("Fight")
                check = auto.locateCenterOnScreen(".\Screenshot\\attack.PNG")
                while check == None:
                    check = auto.locateCenterOnScreen(".\Screenshot\\attack.PNG")
                auto.scroll(-100)
                time.sleep(2)
                cha1Cast1()
                time.sleep(0.8)
                cha1Cast2()
                time.sleep(0.8)
                attack()
                time.sleep(1)
                auto.click(auto.locateCenterOnScreen(".\Screenshot\\raidButton.PNG"))
                auto.move(0,50)
                if auto.locateCenterOnScreen(".\Screenshot\check.PNG") != None:
                    while auto.locateCenterOnScreen(".\Screenshot\check.PNG") != None:
                        getReward()
                        time.sleep(1)
                time.sleep(2)
                auto.scroll(-100)
                joined = len(list(auto.locateAllOnScreen(".\Screenshot\joined.PNG")))
                print(joined)
                print("FightEND")
        else:
            print ("in Reload")
            auto.click(auto.locateCenterOnScreen(".\Screenshot\\raidButton.PNG"))
            auto.move(0,50)
            time.sleep(3)
    else:
        while joined == 3:
            if auto.locateCenterOnScreen(".\Screenshot\check.PNG") != None:
                while auto.locateCenterOnScreen(".\Screenshot\check.PNG") != None:
                    getReward()
                    time.sleep(1)
            print ("Check Dupe")
            auto.hotkey('f5')
            time.sleep(5)
            auto.scroll(-100)
            joined = len(list(auto.locateAllOnScreen(".\Screenshot\joined.PNG")))
    