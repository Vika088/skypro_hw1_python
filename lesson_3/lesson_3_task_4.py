import turtle

pen = turtle.Turtle()
pen.speed(3)


def ring(col, rad):
    # Set the fill
    pen.fillcolor(col)
    # Start filling the color
    pen.begin_fill()
    # Draw a circle
    pen.circle(rad)
    # Ending the filling of the color
    pen.end_fill()


# head
pen.up()
pen.setpos(0, 30)
pen.down()
ring('gray', 80)

# first eye
pen.up()
pen.setpos(-30, 90)
pen.down
ring('white', 10)
pen.up()
pen.setpos(-30, 92)
pen.down
ring('black', 9)

# second eye
pen.up()
pen.setpos(30, 90)
pen.down()
ring('white', 10)
pen.up()
pen.setpos(30, 92)
pen.down()
ring('black', 9)

# nose
pen.up()
pen.setpos(0, 70)
pen.down
ring('black', 8)
pen.up()
pen.setpos(0, 76)
pen.down
ring('black', 10)

# mouth
pen.up()
pen.setpos(0, 65)
pen.down()
pen.right(90)
pen.circle(6, 180)
pen.up()
pen.setpos(0, 65)
pen.down()
pen.left(360)
pen.circle(6, -180)

# first ear
pen.up()
pen.setpos(-95, 160)
pen.down
ring('black', 30)
pen.up()
pen.setpos(-70, 140)
pen.down
ring('grey', 10)

# second ear
pen.up()
pen.setpos(50, 157)
pen.down()
ring('black', 30)
pen.up()
pen.setpos(53, 142)
pen.down
ring('grey', 10)

pen.hideturtle()
pen.screen.exitonclick()
pen.screen.mainloop()
