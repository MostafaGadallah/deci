import random
import time
def print_pause(text): #print the text and wait for 1 second
    print(text)
    time.sleep(0) #pause the execution for 1 second

def input_pause(text): #input the text and wait for 1 second
    user_input=input(text)
    time.sleep(0) #pause the execution for 1 second
    return user_input

def start(): #define a function to start the game
    global monster_name
    print_pause("-------------------- * Adventure game * -------------------")
    monster_name=monster()
    print_pause("You stuck forest and found a "+ monster_name)
    print_pause("He is hungry and wants to kill you but he gave you a chance")
    print_pause("If you answer the question correctly, it will let you live")
    print_pause("you have 20 question")
    print_pause("you have 20 second for answer each question ")
    print_pause("there is another monster come to kill you be fast")
    print_pause("good luck for you")
    get_type() #get the Type of the question from user input

def monster():
    return random.choice(["lion","Gorila","snake","thief"])

def get_type(): #asks the user for the type of calculations
    global game_type #make game type global to use in rand function
    print_pause("you can guess the result (result)")
    print_pause("or you can compare and choose the bigger (compare)")
    game_type=input_pause("select type of calculations result , compare:")
    while game_type.lower() not in ["compare","result"]: #check is valid
        print_pause("Wrong type") #print an error message
        game_type=input_pause("select type of calculations result , compare:")
    get_operator() #get the operator from user input

def get_operator(): #asks the user for the operation of calculations
    global operator #make operator global to use in rand function
    operator = input_pause("select operator of calculations + - * / :")
    while operator not in ["+", "-", "*", "/"]: #check if the input is valid
        print_pause("Wrong operator") #print an error message
        operator = input_pause("select operator of calculations + - * / :")
    if game_type=="compare":
        compare_game()
    elif game_type=="result":
        round_game()

def compare_game(): #start the compare game
    score = 0
    start_total_time = time.time() #start counting the time for all program
    for i in range(20):
        global res1, res2 #make these variables global
        print_pause("question numper " + str(i+1)) #print the question number
        rand() #generate random numbers
        calculation1 = calculation
        res1 = res
        print_pause("calculation 1 :" + calculation1)
        rand()#generate another random numbers
        calculation2 = calculation
        res2 = res
        print_pause("calculation 2 :" + calculation2)
        check_answer_compare()
        score += 1 #add the score by 1
        print_pause("your score is :" + str(score)) #print the current score
    print_pause("Nooooo you beat me")
    print_pause("Iam sure I will beat you next time")
    total_time=str(round(time.time() - start_total_time,1))
    print_pause("you keep alive for "+total_time+"seconds")
    finish() #asks the user if he need to end the game

def round_game(): #start the round game
    score = 0
    start_total_time = time.time() #start counting the time for all program
    for i in range(20):
        global res1#make these variables global to use in answer functions
        print_pause("question numper " + str(i+1)) #print the question number
        rand() #calling rand function to generate random numbers
        res1 = res
        print_pause("calculation is:" + calculation)
        check_answer_round()
        score += 1 #add the score by 1
        print_pause("your score is :" + str(score)) #print the current score
    print_pause("Nooooo you beat me")
    print_pause("Iam sure I will beat you next time")
    total_time=str(round(time.time() - start_total_time,1))
    print_pause("you keep alive for "+total_time+"seconds")
    finish() #asks the user if he need to end the game

def rand():#generating a random calculation
        global calculation , res #make the calculation and the res global
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
    while userinput not in ["1" ,"2","="]:
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

def check_answer_round(): #chek if result is true
    start_time=time.time() #start counting the time
    userinput= input_pause("guees the result:")
    while userinput.isdigit()!=True: #chek that is number
        print_pause("not valid input")
        userinput=input_pause("guees the result:")
    check_time(start_time) #check the time
    if int(userinput) == round(res1,0) :
        print_pause(monster_name +": your answer is True iam angry")
    else :
        print(round(res1,0))
        print_pause(monster_name +": yessss your answer is False")
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
