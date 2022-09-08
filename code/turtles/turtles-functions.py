import turtle
    
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
    t.penup()
    t.goto(x,y)
    t.width(w)
    t.color(color)
    t.pendown()
    # draw a square
    for i in range(4):
        t.forward(sidelen)
        t.right(90)

#def triangle(fill in these):
#    #code to draw the triangle
    
#def ngon(t,numsides,x,y,color,width,sidelen):
#    #code to draw the ngon

wn = turtle.Screen()

crush = turtle.Turtle()

square(crush,0,0,1,"green",50)

squirt = turtle.Turtle()
square(squirt,100,100,5,"red",80)
square(crush,-50,30,3,"yellow",100)
crush.setheading(45)
square(crush,150,30,2,"blue",60)
wn.exitonclick()
wn.mainloop()
