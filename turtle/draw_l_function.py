import turtle

def	drawL(col, height):
	turtle.color(col)
	turtle.pensize(10)
	turtle.right(90)
	turtle.forward(height)
	turtle.left(90)
	turtle.forward(height - 20)


drawL("green", 250) # calling the function
turtle.done()
