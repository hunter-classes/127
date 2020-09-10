import turtle

import shapes
print("This program is going to use shapes")

def main():
    wn = turtle.Screen()
    crush = turtle.Turtle()
    crush.shape("turtle")
    crush.color("green")
    shapes.draw_shape(crush,200,200,10,65,"blue")
    wn.exitonclick()

    wn.mainloop()
    
    
    
#main()
