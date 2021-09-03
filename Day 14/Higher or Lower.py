import random
from art import logo,vs 
from data import data
from replit import clear

playon=True
B=random.choice(data)
score=0

while playon:
    print(logo)
    if score>0:
        print(f"You're right! Current score: {score}")
    A=B
    B=random.choice(data)
    print(f"Compare A: {A['name']}, a {A['description']} from {A['country']}\n{vs}")
    print(f"Against B: {B['name']}, a {B['description']} from {B['country']}")
    guess=input("Who do you think has more followers? Type 'A' or 'B': ").upper()
    if(guess=='A' and A['follower_count']<B['follower_count']):
        playon=False
        break
    elif(guess=='B' and A['follower_count']>B['follower_count']):
        playon=False
        break
    else:
        score=score+1
        clear()
clear()
print(logo)
print(f"Sorry, that's wrong. Final Score: {score}")
