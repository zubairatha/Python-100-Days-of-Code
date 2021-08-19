print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
dec1=input("You're at a cross road. Where do you want to go? Type \"left\" or \"right\"\n").lower()
if dec1=="left":
    dec2=input("You come to a lake. There's an island at the middle of the lake. Type \"wait\" to wait for a boat or \"swim\" to swim across the lake.\n").lower()
    if dec2=="wait":
        dec3=input("You reach the island unharmed. There's a house with 3 doors leading to 3 rooms. One red, one yellow and one blue. Which colour do you choose?\n").lower()
        if dec3=="yellow":
            print("You found the treasure! Congratulations! You win!")
        elif dec3=="red":
            print("You were burned by the fire inside the room. Game Over!")
        elif dec3=="blue":
            print("The room was full of beasts! Game Over!")
        else:
            print("This door doesn't exist. Game over!")
    else:
        print("You were attacked by a trout. Game over!")
else:
    print("You fell into a hole. Game over!")
