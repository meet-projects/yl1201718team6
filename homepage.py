from turtle import *


getscreen().setup(1.0,1.0)
penup()
hideturtle()


def choose_screen(screen_num):
	desicion=int(input("What would you like to do?"))
	if screen_num==0:
		if desicion==1:
			#connect_four()
			print("1")

		if desicion==2:
			#snake()
			print("1")

		if desicion==3:
			#pac_man()
			print("1")

		if desicion==4:
			screen2() 
			print("1")


	elif screen_num==1:
		if desicion==0:
			screen1()

		if desicion==1:
			#agario()
			print("1")

		if desicion==2:
			#memory_game()
			print("1")

		if desicion==3:
			#bubble_burst()
			print("1")

		if desicion==4:
			screen3()
			print("1")

	elif screen_num==2:
		if desicion==0:
			screen2()
			print("1")

		if desicion==1:
			#football()
			print("1")

		if desicion==2:
			#tic_tac_toe()
			print("1")
			
		if desicion==3:
			#pong()
			print("1")


def screen1():
	goto(-125,150)
	write("GAME X", move=False, align="left", font=("Arial", 50, "bold"))
	goto(-95,110)
	write("Choose a game", move=False, align="left", font=("Arial", 20, "normal"))
	goto(-500,0)
	write("Connect four(1)", move=False, align="left", font=("Arial", 20, "normal"))
	goto(-110,0)
	write("Snake(2)", move=False, align="left", font=("Arial", 20, "normal"))
	goto(250,0)
	write("Pac man (3)", move=False, align="left", font=("Arial", 20, "normal"))
	goto(450,-100)
	write("More games(4)", move=False, align="left", font=("Arial", 18, "normal"))
	choose_screen(0)



def screen2():
	clear()
	goto(-95,110)
	write("Choose a game", move=False, align="left", font=("Arial", 20, "normal"))
	goto(-500,0)
	write("Agario(1)", move=False, align="left", font=("Arial", 20, "normal"))
	goto(-110,0)
	write("Memory(2)", move=False, align="left", font=("Arial", 20, "normal"))
	goto(250,0)
	write("Bubble burst(3)", move=False, align="left", font=("Arial", 20, "normal"))
	goto(450,-100)
	write("More games(4)", move=False, align="left", font=("Arial", 18, "normal"))
	goto(-550,-100)
	write("Go back(0)", move=False, align="left", font=("Arial", 18, "normal"))
	choose_screen(1)

def screen3():
	clear()
	goto(-95,110)
	write("Choose a game", move=False, align="left", font=("Arial", 20, "normal"))
	goto(-500,0)
	write("Football(1)", move=False, align="left", font=("Arial", 20, "normal"))
	goto(-110,0)
	write("Tic tac toe(2)", move=False, align="left", font=("Arial", 20, "normal"))
	goto(250,0)
	write("Pong(3)", move=False, align="left", font=("Arial", 20, "normal"))
	goto(450,-100)
	write("Go back(0)", move=False, align="left", font=("Arial", 18, "normal"))
	choose_screen(1)


screen1()


mainloop()