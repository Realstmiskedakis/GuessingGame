'''
@Author: Stelios Miskedakis - @Realstmiskedakis / @Acidshell.gr
Language: Python '3.10.5'
Version: '1.0V'
About this program:

This program is a Guessing Number game that ask  the user's data and then the program says if the program's number is either lower or higher
when the user finds the program's number then the code ends..

'''

# Packages / Libraries
import os
import random

# A list of numbers from 0 to 30.
numbers_list = [0, 1, 2, 3,
                4, 5, 6,
                7, 8, 9,
                10, 11, 12,
                13, 14, 15,
                16, 17, 18,
                19, 20, 21,
                22, 23, 24,
                25, 26, 27,
                28, 29, 30]


# The Guessing Function
def guessing():
    """
    The computer selects a number from 0 to 30, and the user has to guess it.
    """
    # Start The Program
    
    os.system('cls')
    attempts = 0
    com_choice = random.choice(numbers_list)  # The Computer selects a number
    
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
