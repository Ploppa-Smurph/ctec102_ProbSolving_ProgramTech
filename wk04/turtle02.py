# from Pearson CTEC-102 Python Book PowerPoint Chap04 pg 26-30
import turtle


# square
for x in range(4):
    turtle.forward(100)
    turtle.right(90)
    
turtle.penup()
turtle.goto(-250, -300) 
turtle.pendown()   
    
# octagon
for x in range(8):
    turtle.forward(100)
    turtle.right(45)
    
turtle.penup()
turtle.goto(250, 350)    
turtle.pendown()

# very interesting shapes -- like spirograph
num_circles = 36   # number of circles to draw
radius = 100       # radius of each circle
angle = 10         # angle to turn

for x in range(num_circles):
    turtle.circle(radius)
    turtle.left(angle)

turtle.pencolor('purple')
turtle.bgcolor('skyblue')
turtle.hideturtle()

#starburst design with 36 straight lines
start_x = 200
start_y = -300
num_lines = 36
line_length = 450
angle = 170

turtle.goto(start_x, start_y)
turtle.pendown()

for x in range(num_lines):
    turtle.forward(line_length)
    turtle.left(angle)

turtle.showturtle()
