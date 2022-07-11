'''
@Author: Stelios Miskedakis - @Realstmiskedakis / @Acidshell.gr
Language: Python '3.10.5'
Version: '1.0V'
About this program:
This program is a Guessing Number game that ask  the user's data and then the program says if the program's number is either lower or higher
when the user finds the program's number then the code ends..
'''

# Packages / Libraries
import random


# The Guessing Function
def guessing():
    """
    The computer selects a number from 0 to 30, and the user has to guess it.
    """
    # Start The Program
    
    attempts = 0
    com_choice = random.randint(0, 30)  # The Computer selects a number
    
    try:
        
        user_guess = int(input((">> Guess the number from 0 to 30: ")))
        while True:
            if user_guess >= 31:
                print("Invalid Input, Rerun the program.")
                quit()
                
            if user_guess == com_choice:
                attempts += 1
                print(f">> You Found it! Your Attempts {attempts}")
                quit()
                
            elif user_guess < com_choice:
                attempts += 1
                print("Higher!")
                
            elif user_guess > com_choice:
                attempts += 1
                print("Lower!")
                
            user_guess = int(input((">> Guess the number from 0 to 30: ")))
            
    # It's a try and except statement that checks if the user inputs a valid input.
    except (ValueError, TypeError, ZeroDivisionError):
        print(">> Invalid Input, Rerun the program.")
        run = False


guessing()
