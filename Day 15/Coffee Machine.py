from data import MENU,resources

def report():
    for i in resources:
        print(f"{i}: {resources[i]}")

def check_availability(type):
    cof=MENU[type]
    ing=cof["ingredients"]
    flag=0
    for i in ing:
        if(resources[i]<ing[i]):
            print(f"Sorry there's not enough {i}")
            flag=1
    return flag

def update_resources(type):
    cof=MENU[type]
    ing=cof["ingredients"]
    for i in ing:
        resources[i]=resources[i]-ing[i]

nextorder=True
quarter=0.25;dime=0.10;nickel=0.05;penny=0.01

while nextorder:
    money=0
    order=input("What would you like? (espresso/latte/cappuccino): ")
    if order=='report':
        report()
    else:
        check=check_availability(order)
        if check==0:
            cof=MENU[order]
            money=money+quarter*int(input("How many quarters?: "))
            money=money+dime*int(input("How many dimes?: "))
            money=money+nickel*int(input("How many nickels?: "))
            money=money+penny*int(input("How many pennies?: "))
            if(money<cof["cost"]):
                print("Sorry not enough money. Money refunded.")
            else:
                update_resources(order)
                print(f"Here is your ${round(money-cof['cost'],2)} in change. ")
                print(f"Here's your {order} ☕.Enjoy!")
    if(input("Type 'q' if you want to quit otherwise enter any key: ").lower()=='q'):
            nextorder=False
 
