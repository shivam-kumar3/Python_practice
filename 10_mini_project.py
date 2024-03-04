# Guess The number

import random

print("Welcome to the game ")





while True:
    guess = input("Enter The Number between 1 to 10:- or Q for quit")
    computer = random.randint(1,10)
    if guess.lower() == "q":
        break
    guess = int(guess)
    if guess == computer:
        print(f"You have Guessed {guess}\ncomputer have guessed {computer}")
        break
    elif guess < computer:
        print(f"You have Guessed {guess}\ncomputer have guessed {computer} ")
    else:
        print(f"You have Guessed {guess}\ncomputer have guessed {computer} ")

print("-----------------------GAME OVER----------------------")



