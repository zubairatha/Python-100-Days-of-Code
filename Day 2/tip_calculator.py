print("Welcome to the tip calculator.")
bill=float(input("What was the total bill? $"))
tip=int(input("What percentage tip would you like to give? 10,12 or 15? "))
people=int(input("How many people to split the bill? "))
bill+=bill*tip/100
each="{:.2f}".format(bill/people)
print(f"Each person should pay: ${each}")

