def turn_right():
    for _ in range(3):
        turn_left()
while front_is_clear():
    move()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
        
