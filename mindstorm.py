import turtle

def draw_square (new_brad) :

	count = 0
	while (count < 4) :
		new_brad.forward(100)
		new_brad.right(90)
		count = count + 1

def draw_art ():

	window = turtle.Screen ()
	window.bgcolor ("red")

	brad = turtle.Turtle ()
	brad.shape("turtle")
	brad.color("black")
	brad.speed(2)

	for i in range (1,37) :
		draw_square(brad)
		brad.right(10)

	window.exitonclick ()

draw_art ()