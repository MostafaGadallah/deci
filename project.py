import random
import time
def print_pause(text): # define a function to print the text and wait for 1 second 
    print(text)
    time.sleep(1) # pause the execution for 1 second

def input_pause(text): # define a function to input the text and wait for 1 second 
    user_input=input(text)
    time.sleep(1) # pause the execution for 1 second
    return user_input

def start(): # define a function to start the game
    print_pause("------------------------ * Math game * ------------------------")
    print_pause("In this game you will test your math skills")
    print_pause("Two calculations will be displayed")
    print_pause("you must choose wich is larger result 1 or 2 or they are equal")
    get_operator() # get the operator from user input by calling get_operator function
    print_pause("you have 20 question")
    print_pause("you have 20 second for answer each question be ready")
    print_pause("good luck for you")
    question() # start the questions

def question(): # define a function to start the question
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
        score += check_answer() # add the score variable by the returned value from check_answer function
        print_pause("your score is :" + str(score)) # print the current score
    print_pause("Now you finish the game and your percentage = " + str(round((score/20)*100)) + " %") # print the final result as a percentage
    end_total_time = time.time() # end counting the time for all program
    total_time = end_total_time - start_total_time # get the total time by subtracting the end time from the start time
    print_pause("your total time = " + str(round(total_time,1)) + " seconds") # print the total time in seconds
    finish() # calling finish function to asks the user if he need to end the game

def check_answer(): # chek if the user answer is true 
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
        added_score=0
        print_pause("your answer is False")
    return added_score 

def add_score(start_time): #if the time is out will make the score 0 else will add the score value by 1
    end_time=time.time()# end counting the time for the question
    if end_time-start_time>20:
        print_pause("time is out and:")
        return 0
    elif end_time-start_time<=20:
        return 1
    
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

def get_operator(): # asks the user for the operation of calculations
    global operator #make operator global to use in rand function
    operator = input_pause("First select operator of calculations + or - or * or / :") # get user input
    while operator not in ["+", "-", "*", "/"]: # check if the input is valid
        print_pause("Wrong operator") # print an error message
        operator = input_pause("First select operator of calculations + or - or * or / :") # ask for input again
    return operator # return the operator

start() #calling the start function to start the game