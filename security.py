import time
import webbrowser
record = False
tusername = "smart_aliens"
tpassword = "break_the_mold"
tfingerprint = ["mega mind"]


def start():
    check()
    while True:
        function = input("what do you need to do :")
        while function not in [
            "livecam", "close_or_open",
            "start_record", "add_finger_print",
            "end_record", "exit", "totem",
            "change_user_name", "change_password"
        ]:
            print("un valid input")
            function = input("what do you need to do :")
        if function == "livecam":
            livecam()
        elif function == "close_or_open":
            close_or_open()
        elif function == "start_record":
            start_record()
        elif function == "end_record":
            end_record()
        elif function == "add_finger_print":
            add_finger_print()
        elif function == "change_user_name":
            change_user_name()
        elif function == "change_password":
            change_password()
        elif function == "totem":
            print("https://bit.ly/44xlI3k")
        elif function == "exit":
            print("your home is secured")
            print("thank you for using our app")
            exit()


def attack():
    call_emergancy()

    lock_door()

    send_notification()


def call_emergancy():
    print("hello we are ")
    print("122 :we will come fast and secure your house")


def lock_door():
    print("the door is locked you are scured")


def send_notification():
    print("notfication:There is a thief trying to penetrate the house", end="")
    print(" and the police have been contacted please be careful")


def check():
    choise = input("credintial or finger print:")
    while choise not in ["finger print", "credintial"]:
        print("un valid input")
        choise = input("credintial or finger print:")
    if choise == "credintial":
        username = input("your user name:")
        pasword = input("your password:")
        while username != tusername or pasword != tpassword:
            print("wrong credintial")
            username = input("your user name:")
            pasword = input("your password:")
    elif choise == "finger print":
        fingerprint = input("enter your finger print:")
        while fingerprint not in tfingerprint:
            print("this finger print not have acsses")
            fingerprint = input("enter your finger print:")


def change_user_name():
    global tusername
    check()
    nusername = input("new username")
    cnusername = input("confirm new username")
    while cnusername != nusername:
        nusername = input("new username")
        cnusername = input("confirm new username")
    tusername = cnusername


def change_password():
    global tpassword
    check()
    npassword = input("new username")
    cnpassword = input("confirm new username")
    while cnpassword != npassword:
        npassword = input("new username")
        cnpassword = input("confirm new username")
    tpassword = cnpassword


def add_finger_print():
    finger_print = input("enter new finger print")
    tfingerprint.append(finger_print)


def livecam():
    # name=input("is there one out door:")
    # while name not in ["yes","no"]:
    #     name=input("is there one out door:")
    # if name =="yes":
    #     print("there is one out door")
    # else:
    #     print("there is no one out door")
    webbrowser.open_new("https://www.bit.ly/3XXXSLE")
    print("https://www.bit.ly/3XXXSLE")


def close_or_open():
    chosie = input("close or open:")
    while chosie not in ["close", "open"]:
        chosie = input("close or open:")
    if chosie == "close":
        print("the door is closed")
    else:
        print("the door is opened")


def storage():
    chosie = input("do you want to enter storage section:")
    while chosie not in ["yes", "no"]:
        chosie = input("do you want to enter storage section:")
    if chosie == "yes":
        print("you are in storage section")
        section = input("fingerprint,photos or videos:")
        while section not in ["fingerprint", "photos", "videos"]:
            section = input("fingerprint,photos or videos:")
        print("you are now in the "+section+" section")
    else:
        print("you are  in main section")


def start_record():
    global record
    chosie = input("do you want to start record:")
    while chosie not in ["yes", "no"]:
        chosie = input("do you want to start record:")
    if chosie == "yes":
        record = True
        print("record started")
        time.sleep(2)
        end_record()
    else:
        record = False
        print("record not started")


def end_record():
    if record:
        chosie = input("do you want to end record:")
        while chosie not in ["yes", "no"]:
            chosie = input("do you want to end record:")
        if chosie == "yes":
            print("record ended")
        else:
            print("record still")
    else:
        print("please start record first")


start()
""""

"""
