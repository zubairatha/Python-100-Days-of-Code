import random
from art import logo
from replit import clear

level={'easy':10,'hard':5}
buffer=0
while(buffer!=1):
    print(logo)
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")

    attempts=level[input("Choose a difficulty. Type 'easy' or 'hard': ").lower()]
    num=random.randint(1,100)
    win=False

    for i in range(attempts):
        guess=int(input("Make a guess: "))
        if(guess==num):
            print(f"You got it! The answer was {num}")
            win=True
            break
        elif(guess<num):
            print("Too low.")
        else:
            print("Too high.")
        print(f"You have {attempts-i-1} attempts left.")

    if not win:
        print(f"You lose. You're out of attempts. The number was {num}")
    if((input("Do you wish to continue? Type 'y' to continue otherwise any other key: ").lower())!='y'):
        buffer=1
    else:
        clear()
