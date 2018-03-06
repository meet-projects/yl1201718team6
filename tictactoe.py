import turtle
from turtle import *
import time

penup()
getscreen().setup(1.0,1.0)
X_CHOICE=[]
Y_CHOICE=[]
CHOOSEN_SPACES=[]

hideturtle()
turtle.penup()
turtle.goto(300,300)
turtle.pendown()
turtle.goto(300,-300)
turtle.goto(-300,-300)
turtle.goto(-300,300)
turtle.goto(300,300)
turtle.penup()
turtle.goto(100,300)
turtle.pendown()
turtle.goto(100,-300)
turtle.penup()
turtle.goto(-100,300)
turtle.pendown()
turtle.goto(-100,-300)
turtle.penup()
turtle.goto(-300,100)
turtle.pendown()
turtle.goto(300,100)
turtle.penup()
turtle.goto(-300,-100)
turtle.pendown()
turtle.goto(300,-100)

turtle.penup()
turtle.goto(-270,280)
turtle.write("1")
turtle.goto(-70,280)
turtle.write("2")
turtle.goto(130,280)
turtle.write("3")
turtle.goto(-270,80)
turtle.write("4")
turtle.goto(-70,80)
turtle.write("5")
turtle.goto(130,80)
turtle.write("6")
turtle.goto(-270,-120)
turtle.write("7")
turtle.goto(-70,-120)
turtle.write("8")
turtle.goto(130,-120)
turtle.write("9")


BOXES=[]


def turn(letter,box):
	if letter%2==0:
		if box==1:
			write("X",)
		# new_letter="X"
		# letter_list=X_CHOICE


	else:
		new_letter="Y"
		color_list=Y_CHOICE
	# position_x=0
	# found=True
	# letter_ones=0
	# while found==True and position_x<5:
	# 	for position_x in range(len(chosen)):
	# 		if position_x.letter=="Y" or position_x=="X":
	# 			chosen[position_x-1].letter=new_letter
	# 			letter_list.append(position_x-1)
	# 			letter_ones=letter+1
	# 	if letter_ones==6:
		
	# 		found=False
	# 		write("Choose a different Box! This one is full!")





turns=0
while turns<9:
	if turns%2==0:	
		turnx=textinput("choose space for X", "Please enter a number")
		if "turnx".isdigit():
			turn(turns,turnx)
	else:
		turny=textinput("choose space for Y", "Please enter a number")
		if "turny".isdigit():
			turn(turns,turny)
	turns=turns+1

if turns==36:
	quit( )

mainloop()

