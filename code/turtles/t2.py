import turtle

def sample_function():
    print("This is a function")
    print("It can be used multiple times")
    
def square():
    crush = turtle.Turtle()
    # draw a square
    for i in range(4):
        crush.forward(50)
        crush.right(90)

    


wn = turtle.Screen()


square()

squirt = turtle.Turtle()
# draw a triangle
squirt.up()
squirt.goto(100,100)
squirt.down()
squirt.color("red")
squirt.width(5)
for i in range(3):
    squirt.forward(50)
    squirt.right(120)


sample_function()
sample_function()
sample_function()

wn.exitonclick()
wn.mainloop()
