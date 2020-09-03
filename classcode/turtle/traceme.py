import turtle

wn = turtle.Screen()
crush  = turtle.Turtle()
squirt = turtle.Turtle()
crush.goto(10,10)
squirt.goto(250,250)

for i in range(3):
    crush.forward(50)
    squirt.forward(50)
    crush.left(30)
    
for c in ["red","green","blue"]:
    squirt.left(90)
    squirt.color(c)
    squirt.forward(100)
    
crush.color("red")
for s in [5,10,20,3]:
    crush.pensize(s)
    crush.forward(100)
    crush.right(50)
    
    

wn.exitonclick()
wn.mainloop()

