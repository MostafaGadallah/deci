import time
# # import webbrowser
tusername = "smart_aliens"
tpassword = "break_the_mold"
rooms = ["living_room", "bed_room1"
         "bed_room2", "bathroom",
         "reception", "kitchen"]


def start():
    check()
    while True:
        function = input("what do you need to do :")
        while function not in [
                "analisys", "exit", "totem", "change_user_name",
                "change_password", "close_or_open", "timer"
        ]:
            print("un valid input")
            function = input("what do you need to do :")
        if function == "analisys":
            analisys()
        elif function == "change_user_name":
            change_user_name()
        elif function == "change_password":
            change_password()
        elif function == "close_or_open":
            choise = input("close or open:")
            while choise not in ["close", "open"]:
                choise = input("close or open:")
            room = input("wich room do you want:")
            while room != "all" and room not in rooms:
                room = input("wich room do you want:")
            close_or_open(choise, room, 0)
        elif function == "timer":
            time = input("enter the time py seconds:")
            while not check_numper(time):
                time = input("enter the time py seconds:")
            time = int(time)
            choise = input("close or open:")
            while choise not in ["close", "open"]:
                choise = input("close or open:")
            room = input("wich room do you want:")
            while room != "all" and room not in rooms:
                room = input("wich room do you want:")
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
    except NameError:
        print("not a numper")
        return False


def analisys():
    num = input("how many devaises do you have:")
    while not check_numper(num):
        num = input("how many devaises do you have:")
    num = int(num)
    devises_names = []
    devises_usages = []
    for i in range(num):
        devise_name = input("devise name:")
        devise_usage = input("devise usage by wats:")
        while not check_numper(devise_usage):
            devise_usage = input("devise usage by wats:")
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
        devise = input("wich devise do you want:")
        if room == "living_room":
            while devise not in ["tv", "lamp", "fan", "all_devises"]:
                print("this devise not in living room")
                devise = input("wich devise do you want:")
        elif room == "bed_room1":
            while devise not in ["tv", "lamp", "fan", "all_devises"]:
                print("this devise not in bed room1")
                devise = input("wich devise do you want:")
        elif room == "bed_room2":
            while devise not in ["computer", "lamp", "fan", "all_devises"]:
                print("this devise not in bed room2")
                devise = input("wich devise do you want:")
        elif room == "bathroom":
            while devise not in ["lamp", "smart_toilet", "smart_dosh",
                                 "smart_water_tap", "all_devises"]:
                print("this devise not in bath room")
                devise = input("wich devise do you want:")
        elif room == "reception":
            while devise not in ["lamp", "softening",
                                 "fan", "radio", "all_devises"]:
                print("this devise not in reception hall")
                devise = input("wich devise do you want:")
        elif room == "kitchen":
            while devise not in ["lamp", "oven", "washing_machine",
                                 "fridge", "freezer", "all_devises"]:
                print("this devise not in kitchen")
                devise = input("wich devise do you want:")
        if choise == "close":
            time.sleep(ntime)
            print("the "+devise+" in the "+room+" is closed")
        elif choise == "open":
            time.sleep(ntime)
            print("the "+devise+" in the "+room+" is opend")


def check():
    username = input("your user name:")
    pasword = input("your password:")
    while username != tusername or pasword != tpassword:
        print("wrong credintial")
        username = input("your user name:")
        pasword = input("your password:")


def change_user_name():
    check()
    nusername = input("new username:")
    cnusername = input("confirm new username:")
    while cnusername != nusername:
        nusername = input("new username:")
        cnusername = input("confirm new username:")
    tusername = cnusername


def change_password():
    check()
    npassword = input("new username:")
    cnpassword = input("confirm new username:")
    while cnpassword != npassword:
        npassword = input("new username:")
        cnpassword = input("confirm new username:")
    tpassword = cnpassword


start()
