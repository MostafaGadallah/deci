import time 
def livecam ():
    name=input("is there one out door:")
    while name not in ["yes","no"]:
        name=input("is there one out door:")
    if name =="yes":
        print("there is one out door")
    else:
        print("there is no one out door")
def close_and_open():
    chosie=input("close or open:")
    while chosie not in ["close","open"]:
        chosie=input("close or open:")
    if chosie == "close":
        print("the door is closed")
    else:
        print("the door is opened")
def storege():
    chosie=input("do you want to enter storage section:")
    while chosie not in ["yes","no"]:
        chosie=input("do you want to enter storage section:")
    if chosie == "yes":
        print("you are in storage section")
        section=input("fingerprint,photos or videos:")
        while section not in ["fingerprint","photos","videos"]:
            section=input("fingerprint,photos or videos:")
        print("you are now in the "+section+" section")    
    else:
        print("you are  in main section")
def start_record():
    global record
    chosie=input("do you want to start record:")
    while chosie not in ["yes","no"]:
        chosie=input("do you want to start record:")
    if chosie == "yes":
        record=True
        print("record started")
        time.sleep(2)
        end_record()
    else:
        record=False
        print("record not started")

def end_record():
    if record ==True:
        chosie=input("do you want to end record:")
        while chosie not in ["yes","no"]:
            chosie=input("do you want to end record:")
        if chosie == "yes":
            print("record ended")
        else:
            print("record still")
    else:
        print("please start record first")
# livecam() 
# close_and_open() 
# storege() 
start_record() 
