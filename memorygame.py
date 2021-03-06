import turtle
import random
import time 
from turtle import *


#################################
########CLAAASSSSSESSS###########
#################################
class Square2(Turtle):
	def __init__(self,size, x, y, color):
		Turtle.__init__(self)
		self.pu()
		self.shape("square")
		self.size = size
		self.shapesize(size)
		self.x = x
		self.y = y
		self.color(color)
		self.goto(x,y)
#square2 is for the covers
class Square(Turtle):
	def __init__(self,shape_name, x, y, color):
		Turtle.__init__(self)
		self.pu()
		self.shape("square")
		self.shape_name=shape_name
		self.x = x
		self.y = y
		self.color(color)
		self.goto(x,y)

class Ball(Turtle):
	def __init__(self,shape_name, x, y ,  color):
		Turtle.__init__(self)
		self.pu()
		self.shape("circle")
		self.shape_name=shape_name
		self.x =x
		self.y = y
		self.color(color)
		self.goto(x,y)


class Arrow(Turtle):
	def __init__(self,shape_name, x,y, color):
		Turtle.__init__(self)
		self.pu()
		self.shape("arrow")
		self.shape_name=shape_name
		self.x=x
		self.y=y
		self.color(color)
		self.goto(x,y)

class Tturtle(Turtle):
	def __init__(self,shape_name, x, y, color):
		Turtle.__init__(self)
		self.pu()
		self.shape("turtle")
		self.shape_name=shape_name
		self.x = x
		self.y = y
		self.color(color)
		self.goto(x,y)

class Triangle(Turtle):
	def __init__(self,shape_name, x, y , color):
		Turtle.__init__(self)
		self.pu()
		self.shape_name=shape_name
		self.x =x
		self.y = y
		self.color(color)
		self.goto(x,y)
#####################################
#####################################
#####################################

x_y = []
top_covers=[]
#######for the end#######
#########################
bottom_covers = []		#
shapes_to_hide = []		#
#########################
shapes1 = []
players = []
colors = ["blue","red","orange","green"]
shapes = [Square,Ball, Arrow, Tturtle,Triangle]
shape_names = ["s","b","a","tu","tr"]
done_with = []

player1 = textinput("What is your name? (Player 1)  ", "Please don't be clever")
player1_score = 0

player2 = textinput("What is your name? (Player 2)  ", "Please don't be clever")
player2_score = 0

running = True
players.append(player1)
players.append(player2)

turtle.bgcolor("black")
spacing = 110
max_height = 3
min_height = -2
max_width = 4
min_width = -4
turtle.ht()
turtle.tracer (0)
turtle.setup( width = 1500, height = 1500, startx = None, starty = None)
numberer = turtle.clone()
numberer.ht()

player1_turtle = turtle.clone()
player1_turtle.ht()
player1_turtle.pu()
player1_turtle.goto(-600,300)
player1_turtle.color("white")
player1_turtle.write(player1 +"'s score is " +str(player1_score),font=("Papyrus", 20, "normal"))
player2_turtle = turtle.clone()
player2_turtle.ht()
player2_turtle.pu()
player2_turtle.goto(400,300) 
player2_turtle.color("white")
player2_turtle.write(player2 +"'s score is " +str(player2_score),font=("Papyrus", 20, "normal"))
turtle.getscreen().update()

for y in range(min_height, max_height):
	for x in range(min_width, max_width):
		cover = Square2(4,x,y,"white")
		cover.goto(x * spacing, y * spacing)
		bottom_covers.append(cover)
i=0
while i < 40:
	randcoverx = random.randint (min_width,3)
	randcovery = random.randint (min_height,2)
	if (randcoverx,randcovery) not in x_y:
		x_y.append((randcoverx,randcovery))
		i+=1


cover_number=1
hi = 0
xandypoint = 0
for g in range (4):

	hii = 0
	for t in range(5):
		shapem_1=[]
		shapem_2=[]
		shapem1 = shapes[hii](shape_names[hii],x_y[xandypoint][0]*110,x_y[xandypoint][1]*110, colors[hi])
		shapem_1.append(shape_names[hii])
		shapem_1.append(x_y[xandypoint][0]*110)
		shapem_1.append(x_y[xandypoint][1]*110)
		shapem_1.append(colors[hi])
		xandypoint+=1
		shapem2 = shapes[hii](shape_names[hii],x_y[xandypoint][0]*110,x_y[xandypoint][1]*110, colors[hi])
		shapem_2.append(shape_names[hii])
		shapem_2.append(x_y[xandypoint][0]*110)
		shapem_2.append(x_y[xandypoint][1]*110)
		shapem_2.append(colors[hi])
		shapes1.append(shapem_1)
		shapes1.append(shapem_2)
		shapes_to_hide.append(shapem1)
		shapes_to_hide.append(shapem2)
		hii +=1
		xandypoint+=1
		
	hi+=1
print(shapes1)
for y in range(min_height, max_height):
	for x in range(min_width, max_width):
		cover1 = Square2(4,x,y,"white")
		cover1.goto(x * spacing, y * spacing)
		top_covers.append(cover1)
		numberer.pu()
		numberer.goto(x * spacing, y * spacing+40)
		numberer.color("red")

		numberer.write(cover_number, font=("Papyrus", 10, "normal"))
		cover_number +=1

		hi+=1
turtle.getscreen().update()

while running == True:
	for t in range(2):
		for r in range (60):
			print(" ")
		print("It's " +players[t] +"'s turn")
		opened=[]
		xcor = []
		ycor =[]
		for i in range (2):

			box = textinput("Which box do you want to open?   ", "Enter a number")
			if int(box)>40:
				while int(box)>40:
					print ("The number you just entered is too big.", "Enter a different number")
					box = textinput("What other box do you want to open?   ", "Choose a different number")
			w = top_covers[int(box)-1]
			if box in opened or (w.xcor(), w.ycor()) in done_with:
				while box in opened:
					print("That is already open")
					box = textinput("What other box do you want to open?   ", "Enter a number")
				
				while (w.xcor(), w.ycor()) in done_with:
					print ("The box you picked has already been won.")
					box = textinput("What other box do you want to open?   ", "Enter a number")
					w = top_covers[int(box)-1]
			opened.append(box)
			x1 = top_covers[int(box)-1].xcor()
			y1 = top_covers[int(box)-1].ycor()
			xcor.append(x1)
			ycor.append(y1)
			top_covers[int(box)-1].ht()
			turtle.getscreen().update()
			
		maybe_same=[]
		for i in range(len(shapes1)):
			for p in range(2):
				if xcor[p] ==shapes1[i][1] and ycor[p]== shapes1[i][2]:
					maybe_same.append(shapes1[i])

		
		if maybe_same[0][0]==maybe_same[1][0] and maybe_same[0][3]==maybe_same[1][3]:
			print("They're the same!!")
			done_with.append((xcor[0],ycor[0]))
			done_with.append((xcor[1],ycor[1]))

			if players[t] == players[0]:
				player1_turtle.clear()
				player1_score+=1
				player1_turtle.goto(-600,300)
				player1_turtle.write(player1 +"'s score is " +str(player1_score),font=("Papyrus", 20, "normal"))
				
			else:
				player2_turtle.clear()
				player2_score+=1
				player2_turtle.goto(400,300)
				player2_turtle.write(player2 +"'s score is " +str(player1_score),font=("Papyrus", 20, "normal"))
		else:
			for i in range (2):
				time.sleep(2)
				top_covers[int(opened[i])-1].showturtle()
				turtle.getscreen().update()
	total_score = player1_score +player2_score
	if total_score==20:
		running= False

time.sleep(3)
for f in range (40):
	shapes_to_hide[f].ht()
	bottom_covers[f].ht()
turtle.pu()
turtle.goto(0,-300)
turtle.color("green")
turtle.write("GAME OVER",font=("Papyrus", 100, "normal"))
turtle.goto(-100,-300)
if player1_score>player2_score:
	turtle.write(player1+" won!!",font=("Papyrus", 50, "normal"))
else:
	turtle.write(player2+" won!!",font=("Papyrus", 50, "normal"))

turtle.getscreen().update()



turtle.mainloop()
