import time
import webbrowser
record = False
tusername = "smart_aliens"
tpassword = "break_the_mold"
tfingerprint = ["mega_mind"]


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
            "livecam", "close_or_open",
            "start_record", "add_finger_print",
            "end_record", "exit", "totem", "check",
            "change_user_name", "change_password"
        ]:
            print("un valid input")
            function = checked_input("what do you need to do :")
        if function == "livecam":
            livecam()
        elif function == "close_or_open":
            close_or_open()
        elif function == "check":
            check()
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
    choise = checked_input("credintial or finger print:")
    while choise not in ["finger_print", "credintial"]:
        print("un valid input")
        choise = checked_input("credintial or finger print:")
    if choise == "credintial":
        username = checked_input("your user name:")
        pasword = checked_input("your password:")
        while username != tusername or pasword != tpassword:
            print("wrong credintial")
            username = checked_input("your user name:")
            pasword = checked_input("your password:")
    elif choise == "finger_print":
        fingerprint = checked_input("enter your finger print:")
        while fingerprint not in tfingerprint:
            print("this finger print not have acsses")
            fingerprint = checked_input("enter your finger print:")
    print("true credintial")


def change_user_name():
    global tusername
    check()
    nusername = checked_input("new username")
    cnusername = checked_input("confirm new username")
    while cnusername != nusername:
        nusername = checked_input("new username")
        cnusername = checked_input("confirm new username")
    tusername = cnusername
    


def change_password():
    global tpassword
    check()
    npassword = checked_input("new password")
    cnpassword = checked_input("confirm new password")
    while cnpassword != npassword:
        npassword = checked_input("new password")
        cnpassword = checked_input("confirm new password")
    tpassword = cnpassword


def add_finger_print():
    finger_print = checked_input("enter new finger print")
    tfingerprint.append(finger_print)


def livecam():
    # name=checked_input("is there one out door:")
    # while name not in ["yes","no"]:
    #     name=checked_input("is there one out door:")
    # if name =="yes":
    #     print("there is one out door")
    # else:
    #     print("there is no one out door")
    # webbrowser.open_new("https://www.bit.ly/3XXXSLE")
    print("https://www.bit.ly/3XXXSLE")


def close_or_open():
    chosie = checked_input("close or open:")
    while chosie not in ["close", "open"]:
        chosie = checked_input("close or open:")
    if chosie == "close":
        print("the door is closed")
    else:
        print("the door is opened")


def storage():
    chosie = checked_input("do you want to enter storage section:")
    while chosie not in ["yes", "no"]:
        chosie = checked_input("do you want to enter storage section:")
    if chosie == "yes":
        print("you are in storage section")
        section = checked_input("fingerprint,photos or videos:")
        while section not in ["fingerprint", "photos", "videos"]:
            section = checked_input("fingerprint,photos or videos:")
        print("you are now in the "+section+" section")
    else:
        print("you are  in main section")


def start_record():
    global record
    chosie = checked_input("do you want to start record:")
    while chosie not in ["yes", "no"]:
        chosie = checked_input("do you want to start record:")
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
        chosie = checked_input("do you want to end record:")
        while chosie not in ["yes", "no"]:
            chosie = checked_input("do you want to end record:")
        if chosie == "yes":
            print("record ended")
        else:
            print("record still")
    else:
        print("please start record first")


start()
"""
credintial
smart_aliens
wrong_password
wrong_user_name
break_the_mold
smart_aliens
break_the_mold
sadkjdakljdkja
livecam
totem
end_record
start_record
yes
no
end_record
yes
add_finger_print
mostafa
check
finger_print
mostafa
change_user_name
credintial
smart_aliens
break_the_mold
three_ais
three_ais
check
credintial
smart_aliens
break_the_mold
three_ais
break_the_mold
change_password
credintial
three_ais
break_the_mold
out_of_the_box
out_of_the_box
check
three_ais
out_of_the_box
close_or_open
open
exit
"""
