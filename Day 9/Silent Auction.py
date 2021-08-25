from replit import clear 
buffer=0
bidders={}
def find_highest(bidders):
    highestbid={};temp=""
    maximum=0
    for key in bidders:
        if(bidders[key]>maximum):
            maximum=bidders[key]
    for key in bidders:
        if(bidders[key]==maximum):
            highestbid[key]=maximum
            temp=key
    if len(highestbid)==1:
        print(f"The winner is {temp} with a bid of ${highestbid[temp]}")
    else:
        print("It's a tie between: ")
        for key in highestbid:
            print(f"{key} : ${highestbid[key]}")
while(buffer!=1):
    print("Welcome to the secret auction program.")
    print('''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
    ''')
    name=input("What's your full name?: ")
    bid=int(input("What's your bid?: $"))
    bidders[name]=bid
    cont=""
    while(cont!="yes" and cont!="no"):
        cont=input("Are there any bidders: 'yes' or 'no': ").lower()
        if(cont=="no"):
            find_highest(bidders)
            buffer=1
        elif(cont=="yes"):
            clear()
        else:
            print("Enter 'yes' or 'no'")
