import random
from replit import clear
from art import logo

def cardgenerator():
    cards=[11,1,2,3,4,5,6,7,8,9,10,10,10]
    return random.choice(cards)
def scoreOf(cards):
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    if sum(cards)==21 and len(cards)==2:
        return 0
    return sum(cards)
def winner(user,comp):
    if user==comp:
        return "Draw 😐"
    elif comp==0:
        return "Lose, your opponent has a Blackjack 😱"
    elif user==0:
        return "Win with a Blackjack 😎"
    elif user>21:
        return "You went over. You Lose 😭"
    elif comp>21:
        return "Opponent went over. You Win 😁"
    elif user>comp:
        return "You Win 😄"
    else:
        return "You Lose 😤"
def blackjack():
    user_cards=[]
    comp_cards=[]
    i=0
    for _ in range(2):
        user_cards.append(cardgenerator())
        comp_cards.append(cardgenerator())

    while i!=1:
        user_score=scoreOf(user_cards)
        comp_score=scoreOf(comp_cards)
        print(f"Your cards: {user_cards}, and your total is: {user_score}.")
        print(f"Computer's first card is {comp_cards[0]}.")

        if user_score==0 or comp_score==0 or user_score>21:
            i=1
        else:
            cont=input("Type 'y' to deal another card, type 'n' to pass: ")
            if cont=="y":
                user_cards.append(cardgenerator())
            else:
                i=1

    while comp_score!=0 and comp_score<17:
        comp_cards.append(cardgenerator())
        comp_score=scoreOf(comp_cards)

    print(f"Your final hand: {user_cards}, and final score: {user_score}.")
    print(f"Computer's final hand: {comp_cards}, and final score: {comp_score}.")
    print(winner(user_score, comp_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")=="y":
    clear()
    print(logo)
    blackjack()
