import random

number = random.randint(1, 50)
guess = 12

while guess != number:

    guess = int(input("Enter Guess:"))

    if (guess < number):
        print("Guess Higher!!!")
    elif (guess > number):
        print("Guess Lower!!!")
    else:
        print("You won!")



