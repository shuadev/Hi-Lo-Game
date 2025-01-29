import os
import random


EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def clear_screen():
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For macOS and Linux
    else:
        _ = os.system('clear')


def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard: ")
    if level.lower() == "hard":
        return HARD_LEVEL_TURNS
    else:
        return EASY_LEVEL_TURNS


def game():
    print('Welcome to Hi-Lo, the Number Guessing Game!')
    turns = set_difficulty()

    print("I'm thinking of a number between 1 and 100.")
    number = random.randint(1, 100)
    # print("P.S: the number is " + str(number))

    def check_answer(input, num, turns):
        if input < num:
            print("Too low.")
            return turns - 1
        elif input > num:
            print("Too high.")
            return turns - 1
        elif input == num:
            print(f"You got it! The answer was {num}.")

    guess = 0
    while guess != number:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, number, turns)
        if turns == 0:
            print("You've run out of guesses, the game is over!")
            return


while True:
    play = input("Do you want to play Hi-Lo? ")
    if play.lower() == "yes":
        clear_screen()
        game()
    elif play.lower() == "no":
        break
    else:
        print("I didn't get that..")
