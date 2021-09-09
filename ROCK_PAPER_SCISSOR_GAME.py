# ROCK , PAPER , SCISSOR GAME

import random

# defining a function for deciding the result of our game
def Game_decider(Computer , Player) :

    # if both player and computer gives the same input 
    if Computer == Player :
        return 'TIE'
    
    # if computer chooses rock as the input
    elif Computer == 'r' :
        if Player == 'p' :
            return 'WIN'
        elif Player == 's' :
            return 'LOSE'
    
    #if computer chooses paper as the input
    elif Computer == 'p' :
        if Player == 's' :
            return 'WIN'
        elif Player == 'r' :
            return 'LOSE'
    
    #if computer chooses scissor as the input
    elif Computer == 's' :
        if Player == 'r' :
            return 'WIN'
        elif Player == 'p' :
            return 'LOSE'

# creating a recursive function for starting game. so that we does not require to run the code again and again
def Try_again(Choice) :
    if Choice.lower() == 'yes' :
         print("Computer's turn :- Rock(r), Paper(p) and Scissor(s) ")
         Random_number = random.randint(1,3)
         if Random_number == 1 :
            Computer = 'r'
         elif Random_number == 2 :
            Computer = 'p'
         elif Random_number == 3 :
            Computer = 's'
         Player = input("Your's turn :- Rock(r), Paper(p) and Scissor(s) ")
         print(f"Computer chooses {Computer}")
         print(f"Player chooses {Player}")
         Result = Game_decider(Computer , Player)
         if Result == 'WIN' :
            print("Hurrah! You won the game ")
         elif Result == 'LOSE' :
            print("Uff! You lose the game ")
         elif Result == 'TIE' :
            print("Shit! The game is drawn ")
         Choice=input("Would you like to play the game again? \t yes/no ")
         return Try_again(Choice)
    elif Choice == 'no' :
         print("Thanks for playing the game ")
    else:
        print('wrong input')
        # asking the player that is he/she wants to play more?
    Choice=input("Would you like to play the game again? \t yes/no ")

    # calling the recursive function
    Try_again(Choice)

# taking computer's input
print("Computer's turn :- Rock(r), Paper(p) and Scissor(s) ")
# setting up a random number with the use of random module
Random_number = random.randint(1,3)
# setting up vaules using random number in if-elif-else conditional expressions
if Random_number == 1 :
    Computer = 'r'
elif Random_number == 2 :
    Computer = 'p'
elif Random_number == 3 :
    Computer = 's'

# taking player's input
Player = input("Your's turn :- Rock(r), Paper(p) and Scissor(s) ")

# showing the input values of both computer and player
print(f"Computer chooses {Computer}")
print(f"Player chooses {Player}")

# calling the function for deciding the winer of the game
Result = Game_decider(Computer , Player)

# declaring the result of the game 
if Result == 'WIN' :
    print("Hurrah! You won the game ")
elif Result == 'LOSE' :
    print("Uff! You lose the game ")
elif Result == 'TIE' :
    print("Shit! The game is drawn ")

# asking the player that is he/she wants to play more?
Choice=input("Would you like to play the game again? \t yes/no ")

# calling the recursive function
Try_again(Choice)