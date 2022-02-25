import turtle

def main():
    turtle.hideturtle()
    square(100, 0, 50, 'red')
    square(-150, -100, 200 ,'blue')
    square(-200, 150, 75, 'green')
    
# square function draws the square

def square(x, y, width, color):
    turtle.penup()    #raise pen
    turtle.goto(x,y)  #move to specified place
    turtle.fillcolor(color) #set fill color from parameters
    turtle.pendown()  #lower the pen
    turtle.begin_fill()  #start the color fill
    for count in range(4):  #draw a square
        turtle.forward(width)
        turtle.left(90)
    turtle.end_fill()   # end the fill to fill the color 
    
#call the function
main()    