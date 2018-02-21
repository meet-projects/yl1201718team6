import turtle
import random
turtle.ht()
turtle.tracer(1)
turtle.penup()

turtle.setup(width = 1900, height = 1000, startx = 0, starty = 0)

pong = turtle.clone()
pong.shape("square")
pong.color('blue')

UP_ARROW = "Up"  
DOWN_ARROW = "Down"

UP_EDGE = 450
DOWN_EDGE = -450
RIGHT_EDGE = 900
LEFT_EDGE = -900

UP = 0
DOWN = 1
direction = UP

UP_EDGE = 450
DOWN_EDGE = -450
RIGHT_EDGE = 900
LEFT_EDGE = -900

def up ():
    global direction
    direction = UP
    print('you pressed the Up key!')

def down ():
    global direction
    direction = DOWN
    print('you pressed the Down key!')

turtle.onkeypress(up,UP_ARROW)
turtle.onkeypress(down,DOWN_ARROW)
turtle.listen()

def move_pong():
    global direction
    my_pos = pong.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]

    elif direction==UP:
        pong.goto(x_pos,SQUARE_SIZE+y_pos)
        print('you moved up')
    elif direction==DOWN:
        pong.goto(x_pos,y_pos-SQUARE_SIZE)
        print('you moved down')
move_pong()