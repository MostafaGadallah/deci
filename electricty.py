import time
import webbrowser
tusername = "smart_aliens"
tpassword = "break_the_mold"
rooms = ["living_room", "bed_room1"
         "bed_room2", "bathroom",
         "reception", "kitchen"]


def checked_input(uinput):
    if uinput == "exit":
        exit()
    else:
        return input(uinput)


def start():
    check()
    while True:
        function = checked_input("what do you need to do :")
        while function not in [
                "analisys", "exit", "totem", "change_user_name",
                "change_password", "close_or_open", "timer", "check"
        ]:
            print("un valid input")
            function = checked_input("what do you need to do :")
        if function == "analisys":
            analisys()
        elif function == "change_user_name":
            change_user_name()
        elif function == "check":
            check()
        elif function == "change_password":
            change_password()
        elif function == "close_or_open":
            choise = checked_input("close or open:")
            while choise not in ["close", "open"]:
                print("un valid input")
                choise = checked_input("close or open:")
            room = checked_input("wich room do you want:")
            while room != "all" and room not in rooms:
                print("un valid input")
                room = checked_input("wich room do you want:")
            close_or_open(choise, room, 0)
        elif function == "timer":
            time = checked_input("enter the time py seconds:")
            while not check_numper(time):
                print("un valid input")
                time = checked_input("enter the time py seconds:")
            time = int(time)
            choise = checked_input("close or open:")
            while choise not in ["close", "open"]:
                print("un valid input")
                choise = checked_input("close or open:")
            room = checked_input("wich room do you want:")
            while room != "all" and room not in rooms:
                print("un valid input")
                room = checked_input("wich room do you want:")
            close_or_open(choise, room, time)
        elif function == "totem":
            print("https://bit.ly/44xlI3k")
        elif function == "exit":
            print("thank you for using our app")
            exit()


def check_numper(number):
    try:
        int(number)
        return True
    except ValueError:
        print("not a numper")
        return False


def analisys():
    num = checked_input("how many devaises do you have:")
    while not check_numper(num):
        num = checked_input("how many devaises do you have:")
    num = int(num)
    devises_names = []
    devises_usages = []
    for i in range(num):
        devise_name = checked_input("devise name:")
        devise_usage = checked_input("devise usage by wats:")
        while not check_numper(devise_usage):
            devise_usage = checked_input("devise usage by wats:")
        devise_usage = int(devise_usage)
        devises_names.append(devise_name)
        devises_usages.append(devise_usage)
    totalusage = 0
    for i in devises_usages:
        totalusage += i
    print(totalusage)
    index = 0
    for i in devises_names:
        res = str(round(devises_usages[index]/totalusage*100))
        print("d"+str(index)+"/"+devises_names[index]+":"+res)
        index += 1


def close_or_open(choise, room, ntime):
    if room == "all":
        if choise == "close":
            time.sleep(ntime)
            print("the all devises is closed")
        else:
            # time.sleep(time)
            time.sleep(ntime)
            print("the devises is opened")
    else:
        devise = checked_input("wich devise do you want:")
        if room == "living_room":
            while devise not in ["tv", "lamp", "fan", "all_devises"]:
                print("this devise not in living room")
                devise = checked_input("wich devise do you want:")
        elif room == "bed_room1":
            while devise not in ["tv", "lamp", "fan", "all_devises"]:
                print("this devise not in bed room1")
                devise = checked_input("wich devise do you want:")
        elif room == "bed_room2":
            while devise not in ["computer", "lamp", "fan", "all_devises"]:
                print("this devise not in bed room2")
                devise = checked_input("wich devise do you want:")
        elif room == "bathroom":
            while devise not in ["lamp", "smart_toilet", "smart_dosh",
                                 "smart_water_tap", "all_devises"]:
                print("this devise not in bath room")
                devise = checked_input("wich devise do you want:")
        elif room == "reception":
            while devise not in ["lamp", "softening",
                                 "fan", "radio", "all_devises"]:
                print("this devise not in reception hall")
                devise = checked_input("wich devise do you want:")
        elif room == "kitchen":
            while devise not in ["lamp", "oven", "washing_machine",
                                 "fridge", "freezer", "all_devises"]:
                print("this devise not in kitchen")
                devise = checked_input("wich devise do you want:")
        if choise == "close":
            time.sleep(ntime)
            print("the "+devise+" in the "+room+" is closed")
        elif choise == "open":
            time.sleep(ntime)
            print("the "+devise+" in the "+room+" is opend")


def check():
    username = checked_input("your user name:")
    pasword = checked_input("your password:")
    while username != tusername or pasword != tpassword:
        print("wrong credintial")
        username = checked_input("your user name:")
        pasword = checked_input("your password:")
    print("true credintial")


def change_user_name():
    global tusername
    check()
    nusername = checked_input("new username:")
    cnusername = checked_input("confirm new username:")
    while cnusername != nusername:
        print("not identicl")
        nusername = checked_input("new username:")
        cnusername = checked_input("confirm new username:")
    tusername = cnusername


def change_password():
    global tpassword
    check()
    npassword = checked_input("new password:")
    cnpassword = checked_input("confirm new password:")
    while cnpassword != npassword:
        print("not identicl")
        npassword = checked_input("new password:")
        cnpassword = checked_input("confirm new password:")
    tpassword = cnpassword


start()
"""
smart_aliens
wrong_password
wrong_user_name
break_the_mold
smart_aliens
break_the_mold
sadkjdakljdkja
analisys
sdsadx
3
tv
asd
4
fan
6
lamp
10
totem
change_user_name
smart_aliens
break_the_mold
three_ais
three_ais
check
smart_aliens
break_the_mold
three_ais
break_the_mold
change_password
three_ais
break_the_mold
out_of_the_box
out_of_the_box
check
three_ais
out_of_the_box
close_or_open
aqsdasd
close
asdasd
all
close_or_open
close
living_room
all_devises
close_or_open
close
bathroom
fan
smart_toilet
timer
qeqweqda
16
aqsdasd
close
asdasd
all
timer
5
close
living_room
all_devises
timer
7
close
bathroom
fan
smart_toilet
exit
"""
