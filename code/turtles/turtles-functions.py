import turtle
    
def square(t):
    # draw a square
    for i in range(4):
        t.forward(50)
        t.right(90)

    


wn = turtle.Screen()

crush = turtle.Turtle()

square(crush)

squirt = turtle.Turtle()
squirt.penup()
squirt.goto(100,100)
squirt.pendown()
squirt.color("red")
squirt.width(5)
square(squirt)

wn.exitonclick()
wn.mainloop()
