def turn_right():
    for i in range(0,3):
        turn_left()

while not is_facing_north():
    turn_left()

while not at_goal():
    for i in range(0,13):
        if not wall_in_front():
            move()
        else:
            turn_left()

        if not wall_on_right():
                turn_right()
                
    if not wall_on_right():
        turn_right()
        move()