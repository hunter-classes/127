import turtle

wn = turtle.Screen()

crush = turtle.Turtle()

# draw a square
crush.forward(50)
crush.right(90)
crush.forward(50)
crush.right(90)
crush.forward(50)
crush.right(90)
crush.forward(50)
crush.right(90)

squirt = turtle.Turtle()

# draw a triangle
squirt.up()
squirt.goto(100,100)
squirt.down()
squirt.color("red")
squirt.width(5)
squirt.forward(50)
squirt.right(120)
squirt.forward(50)
squirt.right(120)
squirt.forward(50)
squirt.right(120)



wn.exitonclick()
wn.mainloop()
