import random
import time
def print_pause(text): # define a function to print the text and wait for 1 second 
    print(text)
    time.sleep(0) # pause the execution for 1 second

def input_pause(text): # define a function to input the text and wait for 1 second 
    user_input=input(text)
    time.sleep(0) # pause the execution for 1 second
    return user_input

def start(): # define a function to start the game
    print_pause("------------------------ * Adventure game * ------------------------")
    monster_name=monster()
    print_pause("You entered a forest and found a "+ monster_name + " in front of you")
    print_pause("He is hungry and wants to kill you but he gave you a chance")
    print_pause("If you answer the question correctly, it will let you live")
    print_pause("you have 20 question")
    print_pause("you have 20 second for answer each question be ready")
    print_pause("good luck for you")
    get_type() # get the Type of the question from user input

def monster():
    return random.choice(["lion","Gorila","snake","thief",])

def get_type(): # asks the user for the type of calculations
    global game_type #make game type global to use in rand function
    print_pause("you can guess the result of calculation (result)")
    print_pause("or you can compare betwen numbers and choose the bigger (compare)")
    game_type = input_pause("select type of calculations result or comparison :") # get user input
    while game_type.lower() not in ["compare","result"]: # check if the input is valid
        print_pause("Wrong type") # print an error message
        game_type = input_pause("select type of calculations result or comparison :") # ask for input again
        # return game_type # return the operator
    get_operator() # get the operator from user input 

def get_operator(): # asks the user for the operation of calculations
    global operator #make operator global to use in rand function
    operator = input_pause("second select operator of calculations + or - or * or / :") # get user input
    while operator not in ["+", "-", "*", "/"]: # check if the input is valid
        print_pause("Wrong operator") # print an error message
        operator = input_pause("second select operator of calculations + or - or * or / :") # ask for input again
    # return operator # return the operator
    if game_type=="compare":
        compare_game()
    elif game_type=="round":
        round_game()
def compare_game(): # define a function to start the question
    start_total_time = time.time() # start counting the time for all program
    score = 0
    for i in range(20): 
        global res1, res2 # make these variables global to use in answer functions
        print_pause("question numper " + str(i+1)) # print the question number
        rand() # calling rand function to generate random numbers
        calculation1 = calculation
        res1 = res 
        print_pause("calculation 1 :" + calculation1)
        rand() # calling rand function again to generate another random numbers
        calculation2 = calculation 
        res2 = res 
        print_pause("calculation 2 :" + calculation2)
        score += check_answer_compare() # add the score variable by the returned value from check_answer_compare function
        print_pause("your score is :" + str(score)) # print the current score
    print_pause("Nooooo you beat me") # print the final result as a percentage
    print_pause("I'm sure I'll beat you next time") # print the final result as a percentage
    print_pause("your total time = " + str(round(time.time - start_total_time,1)) + " seconds") # print the total time in seconds
    finish() # calling finish function to asks the user if he need to end the game

def round_game(): # define a function to start the question
    start_total_time = time.time() # start counting the time for all program
    score = 0
    for i in range(20): 
        global res1# make these variables global to use in answer functions
        print_pause("question numper " + str(i+1)) # print the question number
        rand() # calling rand function to generate random numbers
        res1 = res 
        print_pause("calculation is:" + calculation)
        score += check_answer_round() # add the score variable by the returned value from check_answer_compare function
        print_pause("your score is :" + str(score)) # print the current score
    print_pause("Nooooo you beat me")
    print_pause("I'm sure I'll beat you next time")
    print_pause("your total time = " + str(round(time.time - start_total_time,1)) + " seconds") # print the total time in seconds
    finish() # calling finish function to asks the user if he need to end the game

def rand():#generating a random calculation
        global calculation , res # make the calculation and the res global to use in the answer function 
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

def check_answer_compare(): # chek if the user answer is true 
    start_time=time.time()
    userinput= input_pause("wich is bigger 1 or 2 or they are = :")
    while userinput not in ["1" ,"2","="]:
        print_pause("not valid input")
        userinput=input_pause("wich is bigger 1 or 2 or they are = :")
    if userinput in["1",">"] and res1>res2 :
        added_score= add_score(start_time) # check the time and add score by 1 if the time is time not out
        print_pause("your answer is True")
    elif userinput in ["2","<"] and res2>res1:
        added_score= add_score(start_time)
        print_pause("your answer is True")
    elif userinput =="=" and res1==res2:
        added_score= add_score(start_time)
        print_pause("your answer is True")
    else :
        add_score(start_time)
        print_pause("yessss your answer is False")
        print_pause("you died hahahaaa")
        finish()
    return added_score 

def check_answer_round(): # chek if the user answer is true 
    start_time=time.time()
    userinput= input_pause("guees the result:")
    while userinput.isdigit()!=True:
        print_pause("not valid input")
        userinput=input_pause("guees the result:")
    if int(userinput) == int(res1) :
        added_score= add_score(start_time) # check the time and add score by 1 if the time is time not out
        print_pause("your answer is True")
    else :
        add_score(start_time)
        print_pause("yaaaa your answer is False")
        print_pause("you died hahahaaa")
        finish()
    return added_score 

def add_score(start_time): #if the time is out will make the score 0 else will add the score value by 1
    end_time=time.time()# end counting the time for the question
    if end_time-start_time>20:
        print_pause("time is out and:")
        return 0
    elif end_time-start_time<=20:
        return 1
def finish(): # ask the user if he want to play more
    play_again=input_pause("Do you want to play again y - n :")
    while play_again.lower() not in ["y","yes","n","no"]:
        print_pause("un valid input")
        play_again=input_pause("Do you want to play again y - n :")
    if play_again.lower() in["y" ,"yes"]: # if user need to play again the game will started again
        print_pause("score more in next game")
        print_pause("Are you ready")
        start()
    elif play_again.lower() in ["n","no"]:  # if user do not need to play again the game will exit
        print_pause("thank you for playing our game")
        exit() #exit the program
start() #calling the start function to start the game
