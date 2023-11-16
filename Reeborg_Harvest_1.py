def start_position():
    for i in range(7):
        move()

def pick_row(n):
    for i in range(n):
        move()
        take()

start_position()
turn_left()
move()
pick_row(6)
turn_left()

for i in range(2):
    pick_row(5)
    turn_left()

for i in range(2):
    pick_row(4)
    turn_left()

for i in range(2):
    pick_row(3)
    turn_left()

for i in range(2):
    pick_row(2)
    turn_left()

for i in range(2):
    pick_row(1)
    turn_left()
