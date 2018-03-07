from turtle import *
import turtle
import random
import os
import subprocess
import time
turtle.tracer(1,0)

getscreen().setup(1.0,1.0)
penup()
hideturtle()
bgcolor("black")




def choose_screen(screen_num):
	desicion=int(textinput("What would you like to do?", "Please enter a number"))
	if screen_num==0:
		if desicion==1:
			child = subprocess.Popen(['python3', 'connectfour.py'])
			while child.poll() is not None:
				print("CONNECT FOUR IS STILL RUNNING GIRL")
				time.sleep(1)

			choose_screen(0)
			print("1")

		if desicion==2:
			child = subprocess.Popen(['python3', 'snake.py'])
			while child.poll() is not None:
				print("SNAKE IS STILL RUNNING GIRL")
				time.sleep(1)

			choose_screen(0)
			print("1")

		if desicion==3:
			child = subprocess.Popen(['python3', 'pacman.py'])
			while child.poll() is not None:
				print("PACMAN IS STILL RUNNING GIRL")
				time.sleep(1)

			choose_screen(0)
			
			print("1")

		if desicion==4:
			screen2() 
			print("1")


	elif screen_num==1:
		if desicion==0:
			screen1()

		if desicion==1:
			child = subprocess.Popen(['python3', 'agario.py'])
			while child.poll() is not None:
				print("AGARIO IS STILL RUNNING GIRL")
				time.sleep(1)

			choose_screen(1)
			print("1")

		if desicion==2:
			child = subprocess.Popen(['python3', 'hangman.py'])
			while child.poll() is not None:
				print("SNAKE IS STILL RUNNING GIRL")
				time.sleep(1)

			choose_screen(1)
			print("1")

		if desicion==3:
			child = subprocess.Popen(['python3', 'bubbleburstcorrect.py'])
			while child.poll() is not None:
				print("FUBBLES IS STILL RUNNING GIRL")
				time.sleep(1)

			choose_screen(1)
			
			print("1")

		if desicion==4:
			screen3()
			print("1")

	elif screen_num==2:
		if desicion==0:
			screen2()
			print("1")

		if desicion==1:
			child = subprocess.Popen(['python3', 'food_drop.py'])
			while child.poll() is not None:
				print("FOOD DROP IS STILL RUNNING GIRL")
				time.sleep(1)

			choose_screen(2)
			print("1")

		if desicion==2:
			child = subprocess.Popen(['python3', 'tictac.py'])
			while child.poll() is not None:
				print("TIC TAC TOE IS STILL RUNNING GIRL")
				time.sleep(1)

			choose_screen(2)
			
			print("1")
			
		if desicion==3:
			child = subprocess.Popen(['python3', 'surprise.py'])
			while child.poll() is not None:
				print("Surprise IS STILL RUNNING GIRL")
				time.sleep(1)

			choose_screen(2)
			print("1")



def screen1():
	clear()
	goto(-225,150)
	pencolor("deepskyblue")
	write("ALL IN ONE", move=False, align="left", font=("Arial", 50, "bold"))
	pencolor("orange")
	goto(-175,110)
	write("Choose a game", move=False, align="left", font=("Arial", 30, "bold"))
	pencolor("darkmagenta")
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
	goto(-125,110)
	pencolor("orange")
	write("Choose a game", move=False, align="left", font=("Arial", 30, "bold"))
	pencolor("darkmagenta")
	goto(-500,0)
	write("Agario(1)", move=False, align="left", font=("Arial", 20, "normal"))
	goto(-110,0)
	write("Hangman(2)", move=False, align="left", font=("Arial", 20, "normal"))
	goto(250,0)
	write("Bubble burst(3)", move=False, align="left", font=("Arial", 20, "normal"))
	goto(450,-100)
	write("More games(4)", move=False, align="left", font=("Arial", 18, "normal"))
	goto(-550,-100)
	write("Go back(0)", move=False, align="left", font=("Arial", 18, "normal"))
	choose_screen(1)

def screen3():
	clear()
	goto(-125,110)
	pencolor("orange")
	write("Choose a game", move=False, align="left", font=("Arial", 30, "bold"))
	pencolor("darkmagenta")
	goto(-500,0)
	write("Food drop(1)", move=False, align="left", font=("Arial", 20, "normal"))
	goto(-110,0)
	write("Tic tac toe(2)", move=False, align="left", font=("Arial", 20, "normal"))
	goto(250,0)
	write("Surprise(3)", move=False, align="left", font=("Arial", 20, "normal"))
	goto(-550,-100)
	write("Go back(0)", move=False, align="left", font=("Arial", 18, "normal"))
	choose_screen(2)


screen1()


mainloop()