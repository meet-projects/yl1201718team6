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
def make_columns(width, listnum):
	global y
	for i in range(6):
		h=turtle.clone()
		columns[listnum].append(h)
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
colored_holes=[1]

columns.append(column0)
columns.append(column1)
columns.append(column2)
columns.append(column3)
columns.append(column4)
columns.append(column5)



pencolor("magenta")

while times<6:

	make_columns(x,times )
	x=x+185
	turtle.goto(x,290)
	y=290
	times=times+1

ht()

def win(testing_color):
	if testing_color=="yellow":
		checking_color=0
		x=0
		y=0
		p=0
		winning=0
		for x in columns:
			for y in x:
				if y.color()[0]=='yellow':
					print("Function works")
					checking_color=checking_color+1
					winning=winning+1
				else:
					winning=0
					print(p)
					print(y)
					p+=1

				if checking_color==4 and winning==4:
					goto(-50,0)
					write("Yellow wins!", move=False, align="left", font=("Arial", 20, "bold"))
					time.sleep(2)
					quit()



		checking_color=0
		winning=0 
		
		for z in range(6):
			for d in range(6):
				if columns[d][z].color()[0]=="yellow":
					checking_color=checking_color+1
					winning=winning+1

				else:
					winning=0

				if checking_color==4 and winning==4:
					goto(-50,0)
					write("Yellow wins!",move=False, align="left", font=("Arial", 20, "bold"))
					time.sleep(2)
					quit()

		check_diag_color="yellow"
		check_diagonal1(check_diag_color,0)
		check_diagonal1(check_diag_color,1)


	if testing_color=="red":
		checking_color=0
		x=0
		y=0
		winning=checking_color
		for x in columns():
			for y in x():
				if y.color()[0]=="red":
					checking_color=checking_color+1
					winning=winning+1
				else:
					winning=0

				if checking_color==4 and winning==4:
					goto(-50,0)
					write("Red wins!",move=False, align="left", font=("Arial", 20, "bold"))
					time.sleep(2)
					quit()



		checking_color=0
		winning=0 
		
		for z in range(6):
			for d in range(6):
				if columns[d][z].color()[0]=="red":
						checking_color=checking_color+1
						winning=winning+1

				else:
					winning=0

					if checking_color==4 and winning==4:
						goto(-50,0)
						write("Red wins!",move=False, align="left", font=("Arial", 20, "bold"))
						time.sleep(2)
						quit()

		check_diag_color="red"
		check_diagonal1(check_diag_color,0)
		check_diagonal1(check_diag_color,1)


def check_diagonal1(colorname, direction):
	print(colorname)
	for j in range(3):
		if direction==0:
			for l in range(3,7,-1):
				if columns[j][l].color()[0]==columns[j-1][l+1].color()[0]==columns[j-2][l+2].color()[0]==columns[j-3][l+3].color()[0]==colorname.lower():
					goto(-50,0)
					write(colorname + " wins!",move=False, align="left", font=("Arial", 20, "bold"))
					time.sleep(2)
					quit()


		else:
			for h in range(3):
				if columns[j][h].color()[0]==columns[j+1][h+1].color()[0]==columns[j+2][h+2].color()[0]==columns[j+3][h+3].color()[0]==colorname.lower():
					goto(-50,0)
					write(colorname+" wins!",move=False, align="left", font=("Arial", 20, "bold"))
					time.sleep(2)
					quit()

def turn(color,colu):
	if color==0:
		new_color="yellow"
		color_list=YELLOW_DISCS
		chosen=columns[colu-1]
		print(chosen)

	else:
		new_color="Red"
		color_list=RED_DISCS
		chosen=columns[colu-1]

	posx=5
	found=True
	color_ones=0
	while found==True and posx!=0:
		if chosen[posx] not in colored_holes:
			print("True")
			chosen[posx].color(new_color)
			found=False
			colored_holes.append(chosen[posx])
			print(colored_holes)
			win(new_color)
		posx=posx-1

		if len(colored_holes)==7:
			found=False

			write("Choose a different column! This one is full!")





turns=0
while turns<36:
	colorturn=turns%2
	if colorturn==0:	
		coly=int(textinput("What column yellow?", "Please enter a number"))
		print(coly)
		turn(colorturn,coly)
	else:
		colrd=int(textinput("What column red?", "Please enter a number"))
		turn(colorturn,colrd)
	turns=turns+1

if turns==36:
	quit( )

mainloop()