import turtle


def f(x):
    print("You sent in :",x)
    print("I do stuff")
    print("I can fo as much as I want")
    for i in ["red","green","blue"]:
        print(i)

def draw_shape(t,x,y,number_sides,side_length,c):
    turn_angle = 360 / number_sides
    t.color(c)
    t.penup()
    t.goto(x,y)
    t.pendown()
    for i in range(number_sides):
        t.forward(side_length)
        t.left(turn_angle)
        
        

wn = turtle.Screen()




#for i in range(number_sides):
#    crush.forward(side_length)
#    crush.left(turn_angle)

crush = turtle.Turtle()
crush.shape("turtle")
crush.color("green")

squirt = turtle.Turtle()
squirt.shape("turtle")
squirt.color("red")

draw_shape(crush,50,50,5,50,"orange")
draw_shape(squirt,200,200,10,65,"blue")
draw_shape(squirt,10,10,3,15,"yellow")
wn.exitonclick()

wn.mainloop()