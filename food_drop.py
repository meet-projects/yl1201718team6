import turtle
import random
#<<<<< HEAD
import time
#=======
unitsize = 20
turtle.tracer(1,0)
turtle.penup()
turtle.hideturtle()

#making the catcher
n=0
m=0
catcher = turtle.clone()

image = "boat_girl.gif"
turtle.addshape("boat_girl.gif")
catcher.shape(image)

#choose a catcher
register_shape=[]


WINDOW_SIZE_X = 500
WINDOW_SIZE_Y = 600
turtle.setup(WINDOW_SIZE_X , WINDOW_SIZE_Y)
turtle.bgpic('sea1.gif')
foodpos_list = []
var=0
SPACEBAR = "space"
#the edges of the screen

UP_EDGE = WINDOW_SIZE_Y/2
DOWN_EDGE = -(WINDOW_SIZE_Y/2) 
RIGHT_EDGE = WINDOW_SIZE_X/2
LEFT_EDGE = -(WINDOW_SIZE_X/2)




turtle_score=turtle.clone()
turtle_score.hideturtle()
turtle_score.goto(-WINDOW_SIZE_X/2+10,-WINDOW_SIZE_Y/2+40)
turtle_score.write('score:'+str(n),font=("Arial",30,("bold","italic")))
turtle_drops = turtle.clone()
turtle_drops.hideturtle()
turtle_drops.goto(-WINDOW_SIZE_X/2+10,-WINDOW_SIZE_Y/2+10)
turtle_drops.write('drops: '+str(m), font=('Arial',30,('bold','italic')))
turtle_story=turtle.clone()
turtle_story.hideturtle()
turtle_story.goto(WINDOW_SIZE_X/2-490,WINDOW_SIZE_Y/2-405)
turtle_story.write("on a stormy windy foggy day...\n \
Jeff the man was sailing in his little boat..\n \
when the wind pushed his boat\n \
to get lost in the fog.. \n \
the next day Jeff woke up,\n \
he was a hungry lost poor man in the\n \
middle of the ocean...\n \
but!  an airplane was passing and luckily\n \
the pilot noticed jeff! \n \
so he threw him a bunch of yummy food!\n \
help jeff catch the food! \n \
be careful! don't make jeff eat the trash!\n \
Enjoy!\n \
press space to continue",font=("Arial",18,("bold","italic")))

SQUARE_SIZE = 20
catcher.goto(-(WINDOW_SIZE_X/2)+150,-(WINDOW_SIZE_Y/2)+120)
catcher.showturtle()

##for i in range (START_LENGTH):
##    x_pos=catcher.pos()[0]
##    y_pos=catcher.pos()[1]
##
##    x_pos=x_pos+SQUARE_SIZE
##
##    my_pos= (x_pos, y_pos)
##    catcher.goto(x_pos, y_pos)
##
##    pos_list.append(my_pos)
##    new_stamp = catcher.stamp()
##    stamp_list.append(new_stamp)


RIGHT_ARROW = 'Right'
LEFT_ARROW = 'Left'
TIME_STEP = 100

RIGHT=0
LEFT=1

def right():
    global direction
    direction= RIGHT
    move_catcher()
    print('you moved right!')
    

def left():
    global direction

    direction = LEFT
    move_catcher()
    print('you moved left!')

turtle.onkeypress(right , RIGHT_ARROW)
turtle.onkeypress(left , LEFT_ARROW)
turtle.listen()

def start():
    global var
    if var==0:
        turtle_story.clear()
        turtle_story.goto(WINDOW_SIZE_X/2-450,WINDOW_SIZE_Y/2-50)
        
        turtle_story.write('FOOD DROP!',font=("Arial",30,("bold","italic")))
        var=1
        falling_food()

turtle.onkeypress(start,SPACEBAR)
##
def move_catcher():
    global direction
    my_pos = catcher.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]
    
    if direction==RIGHT:
        catcher.goto(x_pos + SQUARE_SIZE*3, y_pos)
        print("You moved right!")
    
    elif direction==LEFT:
        catcher.goto(x_pos - SQUARE_SIZE*3, y_pos)
        print("You moved left!")

    if x_pos<=-250:
       right()

    elif x_pos>=250:
       left()

##    my_pos=catcher.pos()
##    pos_list.append(my_pos)
##    new_stamp = catcher.stamp()
##    stamp_list.append(new_stamp)
##
##    old_stamp = stamp_list.pop(0)
##    catcher.clearstamp(old_stamp)
##    pos_list.pop(0)
##
food_type_list=['food-chicken_nagets.gif','food-hotdog.gif','food-coffie.gif','food-chicken.gif','food-hamburger.gif', 'food-icecream.gif','food-sandwish.gif', 'food-pizza.gif']#'food-chicken_nugets'#]
food_list = []
step = 25
bottom = -WINDOW_SIZE_Y/2 + 50
turtle.register_shape('food-chicken_nagets.gif')
turtle.register_shape('food-hotdog.gif')
turtle.register_shape('food-coffie.gif')
turtle.register_shape('food-chicken.gif')
turtle.register_shape('food-hamburger.gif')
turtle.register_shape('food-icecream.gif')

turtle.register_shape('food-pizza.gif')
turtle.register_shape('food-sandwish.gif')
#turtle.register_shape('food-icecream.gif')
def create_food():
    y_pos = WINDOW_SIZE_Y/2 - 50
    min_x = -int(WINDOW_SIZE_X/2/unitsize)+1
    max_x = int(WINDOW_SIZE_X/2/unitsize)-1
    x_pos = random.randint(min_x,max_x)*unitsize
    food = turtle.clone()
    chosen = random.randint(0,len(food_type_list)-1)
    food.shape(food_type_list[chosen])
    food.goto(x_pos,y_pos)
    food.showturtle()
    food_list.append(food)
food_delay = 0
delay_num = 7
fast_turtle = turtle.clone()
trash_list = []
def create_trash():
    y_pos = WINDOW_SIZE_Y/2 - 50
    min_x = -int(WINDOW_SIZE_X)+1
    max_x = int(WINDOW_SIZE_X/2/unitsize)-1
    x_pos = random.randint(min_x,max_x)*unitsize
    trash = turtle.clone()
##    chosen = random.randint(0,len(food_type_list)-1)
##    trash.shape(trash_type_list[chosen])
    turtle.register_shape("trash-bag.gif")
    trash.shape("trash-bag.gif")
    trash.goto(x_pos,y_pos)
    trash.showturtle()
##    trash.shape("square")
    trash_list.append(trash)
trash_delay = 0
delay_num_t = 1
    
def falling_food():
    global food_delay, m, n, delay_num
    food_destroy = []
    eaten_food = []
    for food in food_list:
        x_pos = food.pos()[0]
        y_pos = food.pos()[1]
        if y_pos >= bottom:
            y_pos = y_pos - step
            food.goto(x_pos,y_pos)
            boat_x = catcher.pos()[0]
            boat_y = catcher.pos()[1]
            if (x_pos >=  boat_x - 50 ) and (x_pos <=  boat_x + 50 ) and (y_pos >=  boat_y - 50 ) and (y_pos <=  boat_y + 20 ):
                ind = food_list.index(food)
                eaten_food.append(ind)
        else:
            ind = food_list.index(food)
            food_destroy.append(ind)

    for ind in food_destroy:
        old_food = food_list.pop(ind)
        old_food.hideturtle()
        del old_food
        m=m+1
        turtle_drops.clear()
        turtle_drops.write('drops: '+str(m), font=('Arial',30,('bold','italic')))

    for ind in eaten_food:
        old_food = food_list.pop(ind)
        old_food.hideturtle()
        del old_food
        n=n+1
        turtle_score.clear()
        turtle_score.write("score:"+str(n),font=("Arial",30,("bold","italic")) )
        #after score=25 food falls faster
        if n==25:
            delay_num = 5
            fast_turtle.write('Now faster!', font=('Arial',30,('bold')))
            time.sleep(1)
            fast_turtle.clear()
        if n==40:
            delay_num = 3
            fast_turtle.hideturtle()
            fast_turtle.penup()
            fast_turtle.goto(-70,0)
            fast_turtle.write('Now super fast!', font=('Arial',30,('bold')))
            time.sleep(1)
            fast_turtle.clear()
        if n==50:
            delay_num = 2
            fast_turtle.hideturtle()
            fast_turtle.penup()
            fast_turtle.goto(-70,0)
            fast_turtle.write('extremely fast!!', font=('Arial',30,('bold')))
            time.sleep(1)
            fast_turtle.clear()
    if food_delay <= delay_num:
        food_delay += 1
    else:
        food_delay = 0
        create_food()

    if m == 5:
        print('game over!')
        turtle.write('game over!',font=('Arial',30,('bold')))
        time.sleep(3)
        print ('you droped 5!')
        quit()

    #falling trash
    global trash_delay, delay_num_t, trash_list
    for trash in trash_list:
        x_pos = trash.pos()[0]
        y_pos = trash.pos()[1]
        if y_pos >= bottom:
            y_pos = y_pos - step
            trash.goto(x_pos,y_pos)
            boat_x = catcher.pos()[0]
            boat_y = catcher.pos()[1]
            if (x_pos >=  boat_x - 50 ) and (x_pos <=  boat_x + 50 ) and (y_pos >=  boat_y - 50 ) and (y_pos <=  boat_y + 20 ):
                turtle.write('game over!',font=('Arial',30,('bold')))
                time.sleep(3)
                quit()
        else:
            trash.hideturtle()
            
    if  trash_delay <= delay_num_t:
        trash_delay += 1
    else:
        trash_delay = 0
        create_trash()
##    create_trash()

    turtle.ontimer(falling_food,100)

    
turtle.mainloop()

#falling_food()


