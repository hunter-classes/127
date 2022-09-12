import turtle


def position_turtle(t,x,y,w,color):
    t.penup()
    t.goto(x,y)
    t.width(w)
    t.color(color)
    t.pendown()
    
    
    
def square(t,x,y,w,color,sidelen):
    """
    Draw a square using the turtle passed into t

    Parameters:
      t       - a turtle
      x,y     - location
      w       - width of side
      color   - color to draw in
      sidelen - length of each side
    Returns:
      nothing
    """
    # set the location, color, and width
    position_turtle(t,x,y,w,color)
    # draw a square
    for i in range(4):
        t.forward(sidelen)
        t.right(90)

def triangle(t,x,y,w,color,sidelen):
    """
    Draw a triangle using the turtle passed into t

    Parameters:
      t       - a turtle
      x,y     - location
      w       - width of side
      color   - color to draw in
      sidelen - length of each side
    Returns:
      nothing
    """
    # set the location, color, and width
    position_turtle(t,x,y,w,color)
    # draw a square
    for i in range(3):
        t.forward(sidelen)
        t.right(120)


def hexagon(t,x,y,w,color,sidelen):
    ngon(t,6,x,y,w,color,sidelen)
    
    
def ngon(t,numsides,x,y,width,color,sidelen):
    position_turtle(t,x,y,width,color)
    for i in range(numsides):
        t.forward(sidelen)
        t.right(360/numsides)

    
    
wn = turtle.Screen()

crush = turtle.Turtle()

square(crush,0,0,1,"green",50)

squirt = turtle.Turtle()
square(squirt,100,100,5,"red",80)
square(crush,-50,30,3,"yellow",100)
crush.setheading(45)
square(crush,150,30,2,"blue",60)

triangle(crush,-100,-50,2,"green",50)
hexagon(crush, 50, 100, 1, "black",50)
ngon(crush,5,80,130,1,"black",80)
ngon(crush,6,-80,-130,2,"red",80)
ngon(crush,100,-120,130,2,"red",5)

wn.mainloop()
