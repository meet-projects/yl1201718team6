import turtle
from turtle import *
import time

penup()
getscreen().setup(1.0,1.0)
turtle.speed(999999)
X_CHOICE=[]
Y_CHOICE=[]
CHOOSEN_SPACES=[]

BOARD=	[[1,2,3],
		 [4,5,6],
		 [7,8,9]]

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





def check_winning():
	for i in range(0,2):
		if BOARD[i][0]==BOARD[i][1]==BOARD[i][2]=='x':
			print("X wins!!")
			turtle.sleep(3)
			quit()

		if BOARD[i][0]==BOARD[i][1]==BOARD[i][2]=='y':
			print("Y wins!!")
			turtle.sleep(3)
			quit()

	for c in range(0,2):
		if BOARD[0][c]==BOARD[1][c]==BOARD[2][c]=="x":
			print("X wins!!")
			turtle.sleep(3)
			quit()

		if BOARD[0][c]==BOARD[1][c]==BOARD[2][c]=="y":
			print("Y wins!!")
			turtle.sleep(3)
			quit()

	if BOARD[0][0]==BOARD[1][1]==BOARD[2][2]=="x" or BOARD[0][2]==BOARD[1][1]==BOARD[2][0]=='x':
			print("X wins!!")
			turtle.sleep(3)
			quit()

	if BOARD[0][0]==BOARD[1][1]==BOARD[2][2]=="y" or BOARD[0][2]==BOARD[1][1]==BOARD[2][0]=='y':
			print("Y wins!!")
			turtle.sleep(3)
			quit()









def turn(letter,box):
	#something in this function is wrong because it won't accept letter and box
	turtle.print(box)
	turtle.print(letter)
	if letter%2==0:
		if box ==1:
			UNADDABLE.append(box)
			turtle.goto(200,200)
			turtle.write("X", move=False, align="left", font=("Arial", 30, "bold"))
			turtle.print("working")
			BOARD[1][box-1]='x'

		elif box==2:
			UNADDABLE.append(box)
			turtle.goto(0,200)
			turtle.write("X", move=False, align="left", font=("Arial", 30, "bold"))
			turtle.print("working")
			BOARD[1][box-1]='x'

		elif box==3:
			UNADDABLE.append(box)
			turtle.goto(-200,200)
			turtle.write("X", move=False, align="left", font=("Arial", 30, "bold"))
			turtle.print("working")
			BOARD[1][box-1]='x'

		elif box==4:
			UNADDABLE.append(box) 
			turtle.goto(200,0)
			turtle.write("X", move=False, align="left", font=("Arial", 30, "bold"))
			print("working")
			BOARD[2][box-1]='x'


		elif box==5:
			UNADDABLE.append(box)
			turtle.goto(0,0)
			turtle.write("X", move=False, align="left", font=("Arial", 30, "bold"))
			turtle.print("working")
			BOARD[2][box-1]='x'

		elif box==6:
			UNADDABLE.append(box)
			turtle.goto(-200,0)
			turtle.write("X", move=False, align="left", font=("Arial", 30, "bold"))
			turtle.print("working")
			BOARD[2][box-1]='x'

		elif box==7:
			UNADDABLE.append(box)
			turtle.goto(-200,-200)
			turtle.write("X", move=False, align="left", font=("Arial", 30, "bold"))
			turtle.print("working")
			BOARD[3][box-1]='x'

		elif box==8:
			UNADDABLE.append(box)
			turtle.goto(0,-200)
			turtle.write("X", move=False, align="left", font=("Arial", 30, "bold"))
			turtle.print("working")
			BOARD[3][box-1]='x'

		else:
			UNADDABLE.append(box)
			turtle.goto(200,-200)
			turtle.write("X", move=False, align="left", font=("Arial", 30, "bold"))
			turtle.print("working")
			BOARD[3][box-1]='x'


	else:
		if box==1:
			UNADDABLE.append(box)
			turtle.goto(200,200)
			turtle.write("Y", move=False, align="left", font=("Arial", 30, "bold"))
			turtle.print("working")
			BOARD[1][box-1]='y'

		elif box==2:
			UNADDABLE.append(box)
			turtle.goto(0,200)
			turtle.write("Y", move=False, align="left", font=("Arial", 30, "bold"))
			turtle.print("working")
			BOARD[1][box-1]='y'

		elif box==3:
			UNADDABLE.append(box)
			turtle.goto(-200,200)
			turtle.write("Y", move=False, align="left", font=("Arial", 30, "bold"))
			turtle.print("working")
			BOARD[1][box-1]='y'

		elif box==4: 
			turtle.goto(200,0)
			turtle.write("Y", move=False, align="left", font=("Arial", 30, "bold"))
			print("working")
			BOARD[2][box-1]='y'

		elif box==5:
			UNADDABLE.append(box)
			turtle.goto(0,0)
			turtle.write("Y", move=False, align="left", font=("Arial", 30, "bold"))
			turtle.print("working")
			BOARD[2][box-1]='y'

		elif box==6:
			UNADDABLE.append(box)
			turtle.goto(-200,0)
			turtle.write("Y", move=False, align="left", font=("Arial", 30, "bold"))
			turtle.print("working")
			BOARD[2][box-1]='y'

		elif box==7:
			UNADDABLE.append(box)
			turtle.goto(-200,-200)
			turtle.write("Y", move=False, align="left", font=("Arial", 30, "bold"))
			turtle.print("working")
			BOARD[3][box-1]='y'

		elif box==8:
			turtle.goto(0,-200)
			turtle.write("Y", move=False, align="left", font=("Arial", 30, "bold"))
			turtle.print("working")
			BOARD[3][box-1]='y'

		else:
			UNADDABLE.append(box)
			turtle.goto(200,-200)
			turtle.write("Y", move=False, align="left", font=("Arial", 30, "bold"))
			turtle.print("working")
			BOARD[3][box-1]='y'
	
	check_winning()


	# 	new_letter="Y"
	# 	color_list=Y_CHOICE
	# # position_x=0
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






for turns in range(9):
	if turns==9:
		write("EVEYONE LOSES!")
		time.sleep(2)
		quit( )

	if turns%2==0:	
		turnx=int(numinput("choose space for X", "Please enter a number"))
		while turnx in UNADDABLE:
			turnx=numinput("choose space for X", "Please enter a number that isn't already chosen!")

		if "turnx".isdigit():
			turn(turns,turnx)
	else:
		turny=int(numinput("choose space for Y", "Please enter a number"))
		while turny in UNADDABLE :
			turny=numinput("choose space for Y", "Please enter a number that isn't already chosen!")

		if "turny".isdigit():
			turn(turns,turny)



mainloop()

