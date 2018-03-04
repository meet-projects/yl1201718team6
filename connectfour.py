import turtle
from turtle import *
import time

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
turtle.speed(999999)
def make_columns(width, list):
	global y
	for i in range(6):
		h=turtle.clone()
		columns[i].append(h)
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

	make_columns(x,columns[times] )
	x=x+185
	turtle.goto(x,290)
	y=290
	times=times+1


def win(testing_color):
	if testing_color=="yellow":
		checking_color=0
		x=0
		y=0
		winning=0
		for x in columns():
			for y in x():
				if y.color=="yellow":
					checking_color=checking_color+1
					winning=winning+1
				else:
					winning=0

				if checking_color==4 and winning==4:
					write("checking_color wins!")
					time.sleep(2)
					quit()



		checking_color=0
		winning=0 
		
		for z in range(6):
			for d in range(6):
				if columns[d][z]=="yellow":
					checking_color=checking_color+1
					winning=winning+1

				else:
					winning=0

				if checking_color==4 and winning==4:
					write("checking_color wins!")
					time.sleep(2)
					quit()







	if testing_color=="red":
		checking_color=0
		x=0
		y=0
		winning=0
		for x in columns():
			for y in x():
				if y.color=="red":
					checking_color=checking_color+1
					winning=winning+1
				else:
					winning=0

				if checking_color==4 and winning==4:
					write("checking_color wins!")
					time.sleep(2)
					quit()



		checking_color=0
		winning=0 
		
		for z in range(6):
			for d in range(6):
				if columns[d][z]=="red":
						checking_color=checking_color+1
						winning=winning+1

				else:
					winning=0

					if checking_color==4 and winning==4:
						write("checking_color wins!")
						time.sleep(2)
						quit()

def turn(color,row):
	if colorturn==0:
		new_color="Yellow"
		color_list=YELLOW_DISCS
		chosen=columns[rowy]
	else:
		new_color="Red"
		color_list=RED_DISCS
		chosen=columns[rowrd]
	position_x=0
	found=True
	color_ones=0
	while found==True and position_x<5:
		for position_x in range(len(chosen)):
			if chosen[position_x].color=="Red" or chosen[position_x].color=="Yellow":
				chosen[position_x-1].color="new_color"
				color_list.append(position_x-1)
				color_ones=color+1
		if color_ones==6:
			found=False
			write("Choose a different column! This one is full!")





turns=0
while turns<36:
	colorturn=turns%2
	if colorturn==0:	
		rowy=int(textinput("What row yellow?", "Please enter a number"))
		print(rowy)
		turn(colorturn,rowy)
	else:
		rowrd=int(textinput("What row red?", "Please enter a number"))
		turn(colorturn,rowrd)
	turns=turns+1

if turns==36:
	quit( )

mainloop()