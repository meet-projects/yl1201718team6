import turtle
import random

turtle.bgcolor("White")
player = turtle.clone()
player.penup()
turtle.setup(width = 1900, height = 1000, startx = 0, starty = 0)

turtle.tracer(3)
turtle.penup()

border = turtle.clone()
border.color('green')
border.goto(-900,450)
border.pendown()
border.goto(900,450)
border.goto(900,-450)
border.goto(-900,-450)
border.goto(-900,450)


turtle.tracer(1,0)

SIZE_X=1800
SIZE_Y=900
turtle.setup(SIZE_X+20,SIZE_Y+20)

turtle.penup()

SQUARE_SIZE=20
START_LENGTH=1
food_time=[]
shape_list=[]
score_list=[]
pos_list=[]
stamp_list=[]
score = 0
rot_time = 11

turtle.hideturtle()

for i in range(START_LENGTH):
    x_pos=player.pos()[0]
    y_pos=player.pos()[1]

    my_pos=(x_pos,y_pos)

    pos_list.append(my_pos)

    stamp1=player.stamp()
    stamp_list.append(stamp1)


UP_ARROW="Up"
LEFT_ARROW="Left"
DOWN_ARROW="Down"
RIGHT_ARROW="Right"
TIME_STEP=100
SPACEBAR='space'
##global score
UP=0
DOWN=1
LEFT=2
RIGHT=3


time_count = []
wall_pos=[]
box=turtle.clone()
box.shape('square')
box.hideturtle()
box.penup()
scoreboard = turtle.clone()
scoreboard.goto(-SIZE_X/2 +40 ,SIZE_Y/2 - 40)
scoreboard.penup()

scoreboard.write('score = 0',font=("Arial", 14, "bold"))
#wall maker
def wall_maker(left_corner,hight,width):
    box.goto(left_corner[0],left_corner[1]-SQUARE_SIZE)
    box.color("black")
    for i in range(hight):
        box.goto(box.pos()[0], box.pos()[1]+SQUARE_SIZE)
        box.stamp()
        wall_pos.append(box.pos())
    for i in range(width-1):
        box.goto(box.pos()[0]+SQUARE_SIZE,box.pos()[1])
        box.stamp()
        wall_pos.append(box.pos())
    for i in range (hight-1):
        box.goto(box.pos()[0],box.pos()[1]-SQUARE_SIZE)
        box.stamp()
        wall_pos.append(box.pos())
    for i in range(width-2):
        box.goto(box.pos()[0]-SQUARE_SIZE,box.pos()[1])
        box.stamp()
        wall_pos.append(box.pos())
    

def draw_box(left_corner, height, width):
    start_x, start_y = left_corner
    box.goto(left_corner)
    for h in range(height):
        # draw horizontal line
        for w in range(width):
            old_x, old_y = box.pos()
            box.goto(old_x + SQUARE_SIZE, old_y)
            box.stamp()
            wall_pos.append(box.pos())
        box.goto(start_x, start_y - ((h+1) * SQUARE_SIZE))
        


left_corner=(-900,-450)
wall_maker(left_corner,46,91)
###maze
##

width=10
hight=10
box.color("black")
draw_box((-660,360), hight, width)
draw_box((-260, -40), hight, width)
draw_box((220, 260), hight, width)

width=10
hight=10
box.color("red")
draw_box((-780, -225), hight, width)
draw_box((640, 320), hight, width)
draw_box((140, -180), hight, width)
UP_EDGE=SIZE_Y/2
DOWN_EDGE=-SIZE_Y/2
RIGHT_EDGE=SIZE_X/2
LEFT_EDGE=-SIZE_X/2


direction=0

def up():
    global direction
    x_pos=player.pos()[0]
    y_pos=player.pos()[1]
    new_pos=(x_pos,y_pos+SQUARE_SIZE)
    if new_pos not in wall_pos:
        direction=UP

    #print("You pressed the up key!")

def down():
    global direction
    x_pos=player.pos()[0]
    y_pos=player.pos()[1]
    new_pos=(x_pos,y_pos-SQUARE_SIZE)
    if new_pos not in wall_pos:
        direction=DOWN
    #print("You pressed the down key!")

def left():
    global direction
    x_pos=player.pos()[0]
    y_pos=player.pos()[1]
    new_pos=(x_pos-SQUARE_SIZE,y_pos)
    if new_pos not in wall_pos:
        direction=LEFT
    #print("You pressed the left key!")

def right():
    global direction
    x_pos=player.pos()[0]
    y_pos=player.pos()[1]
    new_pos=(x_pos+SQUARE_SIZE,y_pos)
    if new_pos not in wall_pos:
        direction=RIGHT
    #print("You pressed the right key!")



turtle.onkeypress(up,UP_ARROW)
turtle.onkeypress(down,DOWN_ARROW)
turtle.onkeypress(left,LEFT_ARROW)
turtle.onkeypress(right,RIGHT_ARROW)
turtle.listen()

food=turtle.clone()
food.shape("circle")
food.hideturtle()
food_pos=[]
food_stamps=[]


def make_food():
    min_x=-int(SIZE_X/2/SQUARE_SIZE)+2
    max_x=int(SIZE_X/2/SQUARE_SIZE)-2
    min_y=-int(SIZE_Y/2/SQUARE_SIZE)+2
    max_y=int(SIZE_Y/2/SQUARE_SIZE)-2
    temp_pos = wall_pos[10]
    food.shape("circle")
    while temp_pos in wall_pos:
        food_x=random.randint(min_x,max_x)*SQUARE_SIZE
        food_y=random.randint(min_y,max_y)*SQUARE_SIZE
        temp_pos= (food_x,food_y)
    
    else:
        food.goto(food_x,food_y)
        food_pos.append((food_x,food_y))
        ran_food_stamp=food.stamp()
        food_stamps.append(ran_food_stamp)
        food_time.append(0)
       


    TIME_STEP2=7000
    turtle.ontimer(make_food,TIME_STEP2)
def rottime():
    for i in range(len(food_time)):
        food_time[i] += 1

    turtle.ontimer(rottime, 1000) 


rot_time = 50
rotfood= turtle.clone()
rotfood.shape('triangle')
rotfood.ht()
rotfood.pu()
rotfoodpos = []
def move_player():
    global score

    my_pos=player.pos()
    x_pos=my_pos[0]
    y_pos=my_pos[1]


    if direction==RIGHT:
        new_pos=(x_pos+SQUARE_SIZE,y_pos)
        if new_pos not in wall_pos:
            player.goto(new_pos)

    if direction==LEFT:
        new_pos=(x_pos-SQUARE_SIZE,y_pos)
        if new_pos not in wall_pos:
            player.goto(new_pos)

    if direction==UP:
        new_pos=(x_pos,y_pos+SQUARE_SIZE)
        if new_pos not in wall_pos:
            player.goto(new_pos)

    if direction==DOWN:
        new_pos=(x_pos,y_pos-SQUARE_SIZE)
        if new_pos not in wall_pos:
            player.goto(new_pos)



    my_pos=player.pos()
    pos_list.append(my_pos)
    new_stamp=player.stamp()
    stamp_list.append(new_stamp)
    old_stamp=stamp_list.pop(0)
    player.clearstamp(old_stamp)
    pos_list.pop(0)



    if player.pos() in food_pos:
        food_ind=food_pos.index(player.pos())
        food.clearstamp(food_stamps[food_ind])
        food_pos.pop(food_ind)
        food_stamps.pop(food_ind)
        food_time.pop(food_ind)
        score = score+1
        score_list.append(score)
        scoreboard.clear()
        scoreboard.write('score='+str(score),font=("Arial", 14, "bold"))
        print('you have eaten the food')
        make_food()
    rotten_food = []
    did_food_rot = False
    for i in range(len(food_time)):
        time = food_time[i]
        food_time[i] = time + 1
        if food_time[i] >= rot_time:
            print(i)
            pos = food.pos()
            food_pos.pop(i)
            old_stamp = food_stamps.pop(i)
            food.clearstamp(old_stamp)
            rotten_food.append(i)
            rotfood.goto(pos)
            rotfood.stamp()
            rotfoodpos.append(pos)
            did_food_rot = True

    for rottime in rotten_food:
        food_time.pop(rottime)

    if did_food_rot:
        make_food()

    if player.pos() in rotfoodpos:
        quit()
            

    turtle.ontimer(move_player, TIME_STEP)
    
move_player()
make_food()

turtle.mainloop()