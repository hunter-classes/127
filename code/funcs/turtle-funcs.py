import turtle
import random

def line(t,x,y,angle,color,len):
    t.setheading(angle)
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.color(color)
    t.forward(len)

def draw_poly(t,numsides,x,y,sidelen,color):

    # go to the right location
    t.penup()
    t.goto(x,y)
    t.color(color)
    t.pendown()

    # loop numsides times
    #    draw by moving forward
    #    turn the right amount
    for side in range(numsides):
        t.forward(sidelen)
        t.right(360/numsides)
    
colors = ["red","green","blue","violet","brown","yellow","black","white"]



wn = turtle.Screen()
crush = turtle.Turtle()
# for i in range(30):
#     line(crush,
#          random.randrange(-100,100),
#          random.randrange(-100,100),
#          random.randrange(360),
#          random.choice(colors),
#          random.randrange(50,100))
# crush.forward(50)
# crush.left(50)
# crush.forward(20)

draw_poly(crush,4,0,0,50,"red")
draw_poly(crush,3,-30,30,60,"green")
draw_poly(crush,5,-85,100,50,"green")
draw_poly(crush,12,-85,-100,50,"green")
draw_poly(crush,100,0,150,20,"blue")
wn.exitonclick()
wn.mainloop()

