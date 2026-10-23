import turtle


def draw_filled_square(side, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    for z in range(4):
        turtle.forward(side)
        turtle.right(90)
    turtle.end_fill()


for side, color in [(200, 'red'), (150, 'orange'), (100, 'yellow'), (50, 'green')]:
    turtle.penup()
    turtle.goto(-side / 2, side / 2)
    turtle.pendown()
    draw_filled_square(side, color)


turtle.done()