# import turtle 
import turtle
turtle.showturtle()
turtle.forward(200)
turtle.left(45)
turtle.forward(125)
turtle.right(57)
turtle.backward(24)
turtle.right(33)
turtle.forward(80)
turtle.setheading(90)
turtle.forward(50)
turtle.setheading(270)
turtle.backward(25)
turtle.right(45)
turtle.forward(100)
# the following will return the turtle's current angle heading
turtle.heading() # returned 225.0 from my current doodle

# to "raise the pen" and move the turtle without drawing a line
turtle.penup()
turtle.forward(70)

# to lower the pen again
turtle.pendown()
turtle.forward(40)


turtle.penup()
turtle.right(35)
turtle.forward(60)
turtle.pendown()
# to draw a circle - use the radius of the circle in pixels
turtle.circle(75)

turtle.penup()
turtle.setheading(180)
turtle.forward(80)
turtle.pendown()
# makes a single dot
turtle.dot()

#make a thicker line
turtle.pensize(5)
turtle.forward(20)
turtle.pensize(2)

# change pencolor
turtle.pencolor('blue')
turtle.forward(20)

turtle.pensize(1)
turtle.pencolor('black')
turtle.forward(20)

#change background color
turtle.bgcolor('gray')

# clear screen
# turtle.clearscreen()

turtle.showturtle() #- use after a clearscreen to show the turtle again
# - setup the canvas size
turtle.setup(1920, 1080)

# we can put turtle directly to any position using cartesian coordinates
turtle.goto(100,50)

turtle.goto(-150, 75)

#return to the center of the graphic window without drawing a line
turtle.penup()
turtle.goto(0, 0)

# turtle can display text also
turtle.goto(-225, -75)
turtle.pencolor("green")
turtle.pensize(3)
turtle.write("Hola, Amigo")

turtle.goto(55, 135)
turtle.pendown()
turtle.circle(40)

#to fill objects with color -- using begin_fill and end_fill commands
turtle.penup()
turtle.goto(-401, -300)
turtle.pendown()
turtle.fillcolor('red')
turtle.begin_fill()
turtle.circle(140)
turtle.end_fill()

