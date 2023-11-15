def turn_right():
    for i in range(3):
        turn_left()

def jump():
    for i in range(6):
        move()
        turn_left()
        move()
        for i in range(2):
            turn_right()
            move()
        turn_left()
jump()
