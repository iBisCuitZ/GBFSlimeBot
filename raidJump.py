import  webbrowser,time,random,sys,pyperclip,pygetwindow
import pyautogui as auto

def attack():
    auto.screenshot()
    check = auto.locateCenterOnScreen(".\Screenshot\\attack.PNG")
    while check is None:
        check = auto.locateCenterOnScreen(".\Screenshot\\attack.PNG")
    auto.click(check,duration=random.uniform(0.01,0.5))
    time.sleep(1)
def selectSummon(summonName):
    print('in Select Summon')
    check = auto.locateCenterOnScreen(".\Screenshot\\"+summonName+".PNG",confidence=0.9)
    time.sleep(2)
    while check == None:
        auto.scroll(-100)
        check = auto.locateCenterOnScreen(".\Screenshot\\"+summonName+".PNG",confidence=0.9)
    auto.click(check,duration=random.uniform(0.01,0.5))
    clickOK()
def clickOK():
    check = auto.locateCenterOnScreen(".\Screenshot\ok.PNG",confidence=0.9)
    if check!=None:
        auto.click(check,duration=random.uniform(0.01,0.5))
    while check is None:
        auto.scroll(-100)
        check = auto.locateOnScreen(".\Screenshot\ok.PNG")
    auto.click(check,duration=random.uniform(0.01,0.5))
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
    while auto.locateCenterOnScreen(".\Screenshot\\1st.PNG",confidence=0.5) == None:
        time.sleep(0.5)
    auto.click(auto.locateCenterOnScreen(".\Screenshot\\1st.PNG",confidence=0.5),clicks=2)
    time.sleep(0.2)
    auto.moveTo(auto.locateCenterOnScreen(".\Screenshot\skillInBar.PNG"))
    time.sleep(0.2)
    auto.click(auto.move(30,30))
    auto.click(auto.locateCenterOnScreen(".\Screenshot\\backButton.PNG"))
    time.sleep(0.5)
def cha1Cast2():
    while auto.locateCenterOnScreen(".\Screenshot\\1st.PNG",confidence=0.5) == None:
        time.sleep(0.5)
    auto.click(auto.locateCenterOnScreen(".\Screenshot\\1st.PNG",confidence=0.5))
    time.sleep(0.2)
    auto.moveTo(auto.locateCenterOnScreen(".\Screenshot\skillInBar.PNG"))
    time.sleep(0.2)
    auto.click(auto.move(90,30))
    auto.click(auto.locateCenterOnScreen(".\Screenshot\\backButton.PNG"))
    time.sleep(0.5)
def back():
    auto.click(auto.locateCenterOnScreen(".\Screenshot\\back.PNG"))
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
callSummon = "kaguya"
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
        auto.moveTo(auto.locateCenterOnScreen(".\Screenshot\\moreOptionIcon.PNG",confidence=0.9))
        time.sleep(0.5)
        auto.click(auto.move(0,80))
        time.sleep(0.5)
        #========GameClients==========#
        print("click enterID")
        auto.click(auto.locateCenterOnScreen(".\Screenshot\\enterID.PNG",confidence=0.9))
        time.sleep(1)
        print("click Join a room")
        auto.moveTo(auto.locateCenterOnScreen(".\Screenshot\\joinARoom.PNG",confidence=0.7))
        print("move down")
        auto.click(auto.move(-250,0))
        time.sleep(1)
        print("pasted")
        auto.hotkey('ctrl','v')
        time.sleep(1)
        print('click join')
        auto.click(auto.locateCenterOnScreen(".\Screenshot\\joinARoom.PNG",confidence=0.7))
        print(auto.locateCenterOnScreen(".\Screenshot\\joinARoom.PNG",confidence=0.7))
        if auto.locateCenterOnScreen(".\Screenshot\\raidNoti.PNG",confidence=0.8) == None and auto.locateCenterOnScreen(".\Screenshot\\battleNoti.PNG",confidence=0.8) == None:
            print("Joinning")
            time.sleep(1)
            #=====SelectSummon=====#
            selectSummon(callSummon)
            time.sleep(0.5)
            if auto.locateCenterOnScreen(".\Screenshot\\raidNoti.PNG",confidence=0.8) == None and auto.locateCenterOnScreen(".\Screenshot\\battleNoti.PNG",confidence=0.8) == None:
                #===== Timeline =====#
                print("jumpStart")
                check = auto.locateCenterOnScreen(".\Screenshot\\attack.PNG")
                while check == None:
                    check = auto.locateCenterOnScreen(".\Screenshot\\attack.PNG")
                # time.sleep(2)
                # cha1Cast1()
                # cha1Cast2()
                # time.sleep(3)
                attack()
                time.sleep(0.5)
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
                print("JumpEND")
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
    