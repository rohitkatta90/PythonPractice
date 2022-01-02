# Project - Number Gessing game
import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
random_number = random.randint(1, 100)
#print(f"Randon number is: {random_number}") 
user_choice = input("Choose a difficulty. type 'easy' or 'hard': ")

NUMBER_OF_ATTEMPTS = 0

if user_choice == "easy":
    NUMBER_OF_ATTEMPTS = 10
elif user_choice == "hard":
    NUMBER_OF_ATTEMPTS = 5

#print(NUMBER_OF_ATTEMPTS)

continue_guessing = True

while NUMBER_OF_ATTEMPTS >=1  and continue_guessing == True:
    print(f"You have {NUMBER_OF_ATTEMPTS} attempt(s) remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess > random_number:
        NUMBER_OF_ATTEMPTS -= 1
        print("Too high.")
        print("Guess again.")
    elif guess < random_number:
        NUMBER_OF_ATTEMPTS -= 1
        print("Too low.")
        print("Guess again.")
    elif guess == random_number:
        continue_guessing = False
        print("You won! You guessed it correctly")
if NUMBER_OF_ATTEMPTS == 0:
    print("You lose!")



