import turtle
from turtle import *
import time

penup()
getscreen().setup(1.0,1.0)
turtle.speed(999999)



BOARD=	[[1,2,3],
		 [4,5,6],
		 [7,8,9]]
win_by_159=[]
win_by_123=[]
win_by_147=[]
win_by_456=[]
win_by_789=[]
win_by_258=[]
win_by_369=[]
win_by_357=[]
WINNNIGG=[]
WINNNIGG.append(win_by_357)
WINNNIGG.append(win_by_159)
WINNNIGG.append(win_by_123)
WINNNIGG.append(win_by_147)
WINNNIGG.append(win_by_456)
WINNNIGG.append(win_by_789)
WINNNIGG.append(win_by_258)
WINNNIGG.append(win_by_369)

UNADDABLE=[]

fillcolor("white")
pencolor("black")


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



player1 = textinput("What's your name??", "Player1")
player2 = textinput("And what's your name??", "Player2")


def check_winning():
	for i in range (8):
		if len (WINNNIGG[i]) == 3:
			
			if WINNNIGG[i][0]== "x" and WINNNIGG[i][1]== "x" and WINNNIGG[i][2]=="x":
				pu()
				goto(-300,0)
				time.sleep(1)
				clear()
				bgcolor("red")
				write(player1 +" WINS!!!(X)", font=("Arial", 60, "normal"))
				time.sleep(2)
				quit( )

			elif WINNNIGG[i][0]== "y" and WINNNIGG[i][1]== "y" and WINNNIGG[i][2]=="y":
				pu()
				goto(-300,0)
				time.sleep(1)
				clear()
				bgcolor("red")
				write(player2 +" WINS!!!(O)", font=("Arial", 60, "normal"))
				time.sleep(2)
				quit( )



for turns in range(5):
	


	
	turnx=str(int(numinput("choose space for X", "Please enter a number")))
	while int(turnx) in UNADDABLE:
		turnx=str(int(numinput("choose space for X", "Please enter a number that isn't already chosen!")))

	if turnx.isdigit():
		turnx = int(turnx)
		if turnx ==1:
			UNADDABLE.append(turnx)

			turtle.goto(-200,200)
			turtle.write("X", move=False, align="left", font=("Arial", 30, "bold"))
			win_by_159.append("x")
			win_by_123.append("x")
			win_by_147.append("x")


		elif turnx==2:
			UNADDABLE.append(turnx)
			turtle.goto(0,200)
			turtle.write("X", move=False, align="left", font=("Arial", 30, "bold"))
			win_by_123.append("x")
			win_by_258.append("x")



		elif turnx==3:
			UNADDABLE.append(turnx)
			turtle.goto(200,200)
			turtle.write("X", move=False, align="left", font=("Arial", 30, "bold"))
			win_by_123.append("x")
			win_by_357.append("x")
			win_by_369.append("x")


		elif turnx==4:
			UNADDABLE.append(turnx) 
			turtle.goto(-200,0)
			turtle.write("X", move=False, align="left", font=("Arial", 30, "bold"))
			win_by_147.append("x")
			win_by_456.append("x")


		elif turnx==5:
			UNADDABLE.append(turnx)
			turtle.goto(0,0)
			turtle.write("X", move=False, align="left", font=("Arial", 30, "bold"))
			win_by_159.append("x")
			win_by_258.append("x")
			win_by_357.append("x")
			win_by_456.append("x")

		elif turnx==6:
			UNADDABLE.append(turnx)
			turtle.goto(200,0)
			turtle.write("X", move=False, align="left", font=("Arial", 30, "bold"))
			win_by_456.append("x")
			win_by_369.append("x")

		elif turnx==7:
			UNADDABLE.append(turnx)
			turtle.goto(-200,-200)
			turtle.write("X", move=False, align="left", font=("Arial", 30, "bold"))
			win_by_147.append("x")
			win_by_789.append("x")
			win_by_357.append("x")

		elif turnx==8:
			UNADDABLE.append(turnx)
			turtle.goto(0,-200)
			turtle.write("X", move=False, align="left", font=("Arial", 30, "bold"))
			win_by_258.append("x")
			win_by_789.append("x")

		else:
			UNADDABLE.append(turnx)
			turtle.goto(200,-200)
			turtle.write("X", move=False, align="left", font=("Arial", 30, "bold"))
			win_by_159.append("x")
			win_by_789.append("x")
			win_by_369.append("x")
		check_winning()

	if turns==4:
		pu()
		goto(-300,0)
		time.sleep(1)
		clear()
		bgcolor("red")
		write("EVEYONE LOSES!", font=("Arial", 60, "normal"))
		time.sleep(2)
		quit( )
	turny=str(int(numinput("choose space for O", "Please enter a number")))
	while int(turny) in UNADDABLE :
		turny=str(int(numinput("choose space for O", "Please enter a number that isn't already chosen!")))

	if turny.isdigit():
		turny = int(turny)
		if turny ==1:
			UNADDABLE.append(turny)

			turtle.goto(-200,200)
			turtle.write("O", move=False, align="left", font=("Arial", 30, "bold"))
			win_by_159.append("y")
			win_by_123.append("y")
			win_by_147.append("y")

		elif turny==2:
			UNADDABLE.append(turny)
			turtle.goto(0,200)
			turtle.write("O", move=False, align="left", font=("Arial", 30, "bold"))
			win_by_123.append("y")
			win_by_258.append("y")

		elif turny==3:
			UNADDABLE.append(turny)
			turtle.goto(200,200)
			turtle.write("O", move=False, align="left", font=("Arial", 30, "bold"))
			win_by_123.append("y")
			win_by_357.append("y")
			win_by_369.append("y")

		elif turny==4:
			UNADDABLE.append(turny) 
			turtle.goto(-200,0)
			turtle.write("O", move=False, align="left", font=("Arial", 30, "bold"))
			win_by_147.append("y")
			win_by_456.append("y")


		elif turny==5:
			UNADDABLE.append(turny)
			turtle.goto(0,0)
			turtle.write("O", move=False, align="left", font=("Arial", 30, "bold"))
			win_by_159.append("y")
			win_by_258.append("y")
			win_by_357.append("y")
			win_by_456.append("y")

		elif turny==6:
			UNADDABLE.append(turny)
			turtle.goto(200,0)
			turtle.write("O", move=False, align="left", font=("Arial", 30, "bold"))
			win_by_456.append("y")
			win_by_369.append("y")
		elif turny==7:
			UNADDABLE.append(turny)
			turtle.goto(-200,-200)
			turtle.write("O", move=False, align="left", font=("Arial", 30, "bold"))
			win_by_147.append("y")
			win_by_789.append("y")
			win_by_357.append("y")

		elif turny==8:
			UNADDABLE.append(turny)
			turtle.goto(0,-200)
			turtle.write("O", move=False, align="left", font=("Arial", 30, "bold"))
			win_by_258.append("y")
			win_by_789.append("y")
		else:
			UNADDABLE.append(turny)
			turtle.goto(200,-200)
			turtle.write("O", move=False, align="left", font=("Arial", 30, "bold"))
			win_by_159.append("y")
			win_by_789.append("y")
			win_by_369.append("y")
		check_winning()
	turtle.getscreen().update()
	


mainloop()