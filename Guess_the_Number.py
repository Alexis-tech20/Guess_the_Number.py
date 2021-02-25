#Guessing the Number Game
#Makes random functions available and helps generate a random number
import random

#Define the function to guess and make x a perimeter for random number
def guess(x):
    random_number = random.randint(1, x)
    guess = 0
#insert a while loop with expression
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
#If statement to tell the user whether they are close to the number of not.
        if guess < random_number:
            print('Sorry, guess again. Too low.')
        elif guess > random_number:
            print('Sorry, guess again. Too high.')
    print(f'Yay, congrats. You have guessed the number {random_number} correctly! ')

#The variable x can only go up to 10. So guess a number between 1-10.Can always be changed
guess(10)
