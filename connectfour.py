import turtle
from turtle import *

penup()
getscreen().setup(1.0,1.0)
RED_DISCS=[]
YELLOW_DISCS=[]
r=30
bgcolor("Navy")
shape("circle")
shapesize(r/10)
color("White")
HOLES=[]
sec=100
goto(-500,290)
y=290
x=-500
def make_columns(width, list):
	global y
	for i in range(6):
		h=turtle.clone()
		HOLES.append(h)
		y=y-125
		goto(width,y)

times=0
columns=[]
column0=[]
column1=[]
column2=[]
column3=[]
column4=[]
column5=[]

columns.append(column0)
columns.append(column1)
columns.append(column2)
columns.append(column3)
columns.append(column4)
columns.append(column5)


while times<6:

	if times==6:
		turtle.hideturtle()

	columns
	make_columns(x,columns[times] )
	x=x+185
	turtle.goto(x,290)
	y=290
	times=times+1

def turn(color,row):
	chosen=columns[row]
	if color==0:
		new_color="Yellow"
		color_list=YELLOW_DISCS
	else:
		new_color="Red"
		color_list=RED_DISCS
	position_x=0
	found=True
	color_ones=0
	while found==True and position_x<5:
		for position_x in range(len(chosen)):
			if position_x.color=="Red" or position_x=="Yellow":
				chosen[position_x-1].color=new_color
				color_list.append(position_x-1)
				color_ones=color+1
		if color_ones==6:
			found=False
			write("Choose a different column! This one is full!")





turns=0
while turns<36:
	if turns%2==0:	
		rowy=input("What row yellow?")
		turn(turns,rowy)
	else:
		rowrd=input("What row red?")
		turn(turns,rowrd)
	turns=turns+1


mainloop()