from turtle import *
import turtle
import time
import random 
from ball import Ball
import math


turtle.hideturtle()
hideturtle()
tracer(0)
colormode(255)
turtle.goto(-100,100)
turtle.write("START GAME", move=False, align="left", font=("Arial", 20, "normal"))
turtle.goto(-150,0)
turtle.write("Eat the other balls to get bigger!", font=("Arial", 16, "normal"))
turtle.goto(-150,-50)
turtle.write("Don't let bigger balls eat you!", font=("Arial", 16, "normal"))
turtle_clone=turtle.clone()
turtle_clone.hideturtle()
turtle_clone.penup()
turtle_clone.goto(-100,100)
time.sleep(2)
turtle.clear()



RUNNING=True
SLEEP=0.0077
SCREEN_WIDTH= getcanvas().winfo_width()/2
SCREEN_HEIGHT= getcanvas().winfo_height()/2
NUMBER_OF_BALLS=5
MINIMUM_BALL_RADIUS=10
MAXIMUM_BALL_RADIUS=60
MINIMUM_BALL_DX=-1
MAXIMUM_BALL_DX=1
MINIMUM_BALL_DY=-1
MAXIMUM_BALL_DY=1
BALLS=[]
MY_BALL=Ball(0,0,0,0,30,"red")
MY_BALL_C=[]



def generate_stats():
	x=random.randint(int(-SCREEN_WIDTH+MAXIMUM_BALL_RADIUS),int(SCREEN_WIDTH-MAXIMUM_BALL_RADIUS))

	y=random.randint(int(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS),int(SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS))
	dx=random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
	
	while dx==0:
		dx=random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
	dy=random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
	
	while dy==0:
		dy=random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
	r=random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)

	while x>0 and x<=0+r:
		x=random.randint(int(-SCREEN_WIDTH+MAXIMUM_BALL_RADIUS),int(SCREEN_WIDTH-MAXIMUM_BALL_RADIUS))
		r=random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)

	color=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
	return (x,y,dx,dy,r,color)
	
for i in range(NUMBER_OF_BALLS):
	(x,y,dx,dy,r,color)=generate_stats()
	BALL1= Ball(x,y,dx,dy,r,color)
	BALLS.append(BALL1)

def move_all_balls():
	for i in BALLS:
		i.move(SCREEN_WIDTH,SCREEN_HEIGHT)



def collide(ball_a,ball_b):
	 if ball_a==ball_b:
	 	return False 
	 r_sum=ball_a.r+ball_b.r
	 center_sum=math.sqrt(math.pow(ball_b.xcor() - ball_a.xcor(),2) + math.pow(ball_b.ycor() - ball_a.ycor(),2))
	 if center_sum+10 <= r_sum:
	 	return True
	 else:
	 	return False

def check_all_balls():
	for ball_a in BALLS:
		for ball_b in BALLS:
			if collide(ball_a,ball_b)==True:
				ball_ar=ball_a.r
				ball_br=ball_b.r
				(x,y,dx,dy,r,color)=generate_stats()
				ball_loser=None
				if ball_br < ball_ar:
					ball_loser=ball_b
					ball_winner=ball_a
					
				else:
					ball_loser=ball_a
					ball_winner=ball_b
				ball_loser.goto(x,y)
				ball_loser.dx=dx
				ball_loser.dy=dy
				ball_loser.shapesize(r/10)
				ball_loser.r=r
				collide(MY_BALL,ball_loser)
				if collide(MY_BALL,ball_loser):
					if MY_BALL.r < ball_loser.r:
						return False 
					else:
						ball_lr=ball_loser.r
						(x,y,dx,dy)=generate_stats()
						ball_loser.goto(x,y)
						ball_loser.dx=dx
						ball_loser.dy=dy
				new_r=ball_winner.r+1
				ball_winner.r=new_r
				ball_winner.shapesize(new_r/10)


def check_myball_collision():
	for i in BALLS:
		collide(MY_BALL,i)
		if collide(MY_BALL,i):
			if MY_BALL.r < i.r:
				turtle_clone.write("YOU LOSE!",align= "left", font=("Arial",30, "normal")) 
				return False
			else:
				ball_ir=i.r
				MY_BALLr=MY_BALL.r
				(x,y,dx,dy,r,color)=generate_stats()
				i.goto(x,y)
				i.dx=dx
				i.dy=dy
				i.shapesize(r/10)
				i.r=r
				new_r2=MY_BALL.r+1
				MY_BALL.r=new_r2
		
				MY_BALL.shapesize(MY_BALL.r/10)
	return True 

def movearound(event):
	x_cord=event.x-SCREEN_WIDTH
	y_cord=SCREEN_HEIGHT-event.y
	MY_BALL.goto(x_cord,y_cord)



getcanvas().bind("<Motion>", movearound)
listen()

while RUNNING==True:
	if SCREEN_WIDTH != getcanvas().winfo_width()/2 or SCREEN_HEIGHT != getcanvas().winfo_height()/2:
		SCREEN_WIDTH = getcanvas().winfo_width()/2
		SCREEN_HEIGHT != getcanvas().winfo_height()/2

	move_all_balls()
	check_all_balls()
	check_myball_collision()
	getscreen().update()
	if check_myball_collision() :
		RUNNING=True
	else: 
		RUNNING=False 
	time.sleep(SLEEP)


mainloop()