import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user=int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))
temp={0:"print(rock)",1:"print(paper)",2:"print(scissors)"}

if(user in [0,1,2]):
    print("You chose:")
    eval(temp[user])
    print("Computer chose:")
    comp=random.randint(0,2)
    eval(temp[comp])
    if((user==0 and comp==2) or (user==1 and comp==0) or (user==2 and comp==1)):
        print("You win :)")
    elif(user==comp):
        print("It's a draw :|")
    else:
        print("You lose :(")
else:
    print("Wrong choice.")
