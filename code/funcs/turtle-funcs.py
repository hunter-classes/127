import turtle
import random

def line(t,x,y,angle,color,len):
    t.setheading(angle)
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.color(color)
    t.forward(len)

colors = ["red","green","blue","violet","brown","yellow","black","white"]

wn = turtle.Screen()
crush = turtle.Turtle()
for i in range(30):
    line(crush,
         random.randrange(-100,100),
         random.randrange(-100,100),
         random.randrange(360),
         random.choice(colors),
         random.randrange(50,100))
# crush.forward(50)
# crush.left(50)
# crush.forward(20)
wn.exitonclick()
wn.mainloop()

