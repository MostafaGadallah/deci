#important this project require download (random , time , decimal) Libraries
import random
import time
from decimal import localcontext, Decimal, ROUND_HALF_UP
def print_pause(text): #print the text and wait for 1 second
    print(text)
    time.sleep(0) #pause the execution for 1 second

def input_pause(text): #input the text and wait for 1 second
    user_input=input(text)
    time.sleep(0) #pause the execution for 1 second
    return user_input

def start(): #define a function to start the game
    global monster_name
    monster_name=monster()
    print_pause("-------------------- * Adventure game * -------------------")
    print_pause("You stuck forest and found a "+ monster_name)
    print_pause("He is hungry and wants to kill you but he gave you a chance")
    print_pause("If you answer the question correctly, it will let you live")
    print_pause("you have 20 question")
    print_pause("you have 20 second for answer each question ")
    print_pause("there is another monster come to kill you be fast")
    print_pause("good luck for you")
    get_type() #get the Type of the question from user input

def monster():
    return random.choice(
        ["Lion","Gorila","Tiger","Dinasour","Chettah","Wolf","Bear"]
        )

def get_type(): #type of calculations
    global game_type #make game type global
    print_pause("you can guess the result (result)")
    print_pause("or you can compare and choose the bigger (compare)")
    game_type=input_pause("select type of calculations result , compare:")
    while game_type.lower() not in ["compare","result"]: #check is valid
        print_pause("Wrong type") #print an error message
        game_type=input_pause("select type of calculations result , compare:")
    get_operator() #get the operator from user input

def get_operator(): #operator of calculations
    global operator #make operator global
    operator = input_pause("select operator of calculations + - * / :")
    while operator not in ["+", "-", "*", "/"]: #check input validity
        print_pause("Wrong operator") #error message
        operator = input_pause("select operator of calculations + - * / :")
    if game_type=="compare":
        compare_game() #start the compare game
    elif game_type=="result":
        result_game() #start the result game

def compare_game(): #start the compare game
    score = 0
    start_total_time = time.time() #start counting the time for all program
    for i in range(20):
        global res1, res2 #make these variables global
        print_pause("question numper " + str(i+1)) #question number
        rand() #generate random numbers
        res1 = res
        print_pause("calculation 1 :" + calculation)
        rand()#generate another random numbers
        res2 = res
        print_pause("calculation 2 :" + calculation)
        check_answer_compare()
        score += 1 #add the score by 1
        print_pause("your score is :" + str(score)) #print the current score
    print_pause(monster_name+" : Nooooo you beat me")
    print_pause(monster_name+" : Iam sure I will beat you next time")
    total_time=str(round(time.time() - start_total_time,1))
    print_pause(monster_name+" : you keep alive for "+total_time+"seconds")
    finish() #asks the user if he need to end the game

def result_game(): #start the result game
    score = 0
    start_total_time = time.time() #start counting the time for all program
    for i in range(20):
        global res1#make these variables global to use in answer functions
        print_pause("question numper " + str(i+1)) #question number
        rand() #calling rand function to generate random numbers
        print_pause("calculation is:" + calculation)
        check_answer_result()
        score += 1 #add the score by 1
        print_pause("your score is :" + str(score)) #print the current score
    print_pause(monster_name+" : Nooooo you beat me")
    print_pause(monster_name+" : Iam sure I will beat you next time")
    total_time=str(round(time.time() - start_total_time,1))
    print_pause(monster_name+" : you keep alive for "+total_time+"seconds")
    finish() #asks the user if he need to end the game

def rand():#generating a random calculation
        global calculation , res #make the calculation , res global
        rand1=random.randrange(10)
        rand2=random.randrange(1,10)
        if operator == "+":
            calculation = str(rand1) + "+" + str(rand2)
            res=rand1+rand2
        elif operator == "-":
            calculation = str(rand1) + "-" + str(rand2)
            res=rand1-rand2
        elif operator == "*":
            calculation = str(rand1) + "*" + str(rand2)
            res=rand1*rand2
        elif operator == "/":
            calculation = str(rand1) + "/" + str(rand2)
            res=rand1/rand2

def check_answer_compare(): #chek if comparing is true
    start_time=time.time() #start counting the time
    userinput= input_pause("wich is bigger 1 or 2 or they are = :")
    while userinput not in ["1" ,"2","=",">","<"]:#check validaty
        print_pause("not valid input")
        userinput=input_pause("wich is bigger 1 or 2 or they are = :")
    check_time(start_time) #check the time
    if userinput in["1",">"] and res1>res2 :
        print_pause("your answer is True")
    elif userinput in ["2","<"] and res2>res1:
        print_pause("your answer is True")
    elif userinput =="=" and res1==res2:
        print_pause(monster_name +": your answer is True iam angry")
    else :
        print_pause(monster_name +": yessss your answer is False")
        print_pause(monster_name +": you died hahahaaa")
        finish()

def check_number(input):
    try:
        return int(input)
    except:
        return "notvalid"

def check_answer_result(): #chek if result is true
    start_time=time.time() #start counting the time
    userinput= input_pause("guees the result:")
    while check_number(userinput)=="notvalid": #chek that is number
        print_pause("not valid input")
        userinput=input_pause("guees the result:")
    check_time(start_time) #check the time
    with localcontext() as ctx:
        ctx.rounding = ROUND_HALF_UP
        ronded_value=Decimal(res).to_integral_value()
    if int(userinput) == ronded_value :
        print_pause(monster_name +": your answer is True iam angry")
    else :
        print_pause(monster_name +": yessss your answer is False")
        print("the true result is :"+str(ronded_value))
        print_pause(monster_name +": you died hahahaaa")
        finish()

def check_time(start_time):
    end_time=time.time()#end counting the time for the question
    if end_time-start_time>20:
        print_pause("yaaaa time is out")
        print_pause("you died hahahaaa")
        finish()

def finish(): #ask the user if he want to play more
    play_again=input_pause("Do you want to play again y - n :")
    while play_again.lower() not in ["y","yes","n","no"]:
        print_pause("un valid input")
        play_again=input_pause("Do you want to play again y - n :")
    if play_again.lower() in["y" ,"yes"]: #if user need to play again
        print_pause("score more in next game")
        print_pause("Are you ready")
        start() #play the game again
    elif play_again.lower() in ["n","no"]: #if user need to exit
        print_pause("thank you for playing our game")
        exit() #exit the program

start() #start the game