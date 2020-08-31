import turtle

    

# Your previous python3 code is preserved below
# print("Hello, world! This is Python 3!")
# 
# for color in ["blue", "red", "green",  "purple"]:
#     # python will run this code once for each value
#     # in the "list." Each time through, the variable
#     # color will be the next value
#     print(color)
#     print("done")
#     print("How many times will this line print")
# print("How many times will this line print")
# 
# sum = 0
# for number in [0,1,2,3]:
#     sum = sum + number
#     print(number,sum)
# 
# sum = 0
# for number in range(4):
#     sum = sum + number
#     print(number,sum)
# 
# for number in range(1,4):
#     print(number)
#     
# # Your previous python3-turtle code is preserved below
# # import turtle
# # 
# # wn = turtle.Screen()
# # 
# # crush = turtle.Turtle()
# # # crush.forward(50)
# # # crush.left(10)
# # # crush.forward(100)
# # crush.shape("turtle")
# # crush.color("green")
# # #crush.forward(40)
# # 
# # # Write the code to have crush draw a square
# # crush.forward(100)
# # crush.left(90)
# # 
# # crush.forward(100)
# # crush.left(90)
# # 
# # crush.forward(100)
# # crush.left(90)
# # 
# # crush.forward(100)
# # crush.left(90)
# # 
# # crushgotoxy(150,20)
# # crush.forward(50)
# # wn.exitonclick()
# # wn.mainloop()

wn = turtle.Screen()

crush = turtle.Turtle()
crush.color("green")
crush.shape("turtle")

#for number in range(0,4):
#    crush.forward(100)
#    crush.left(90)
for c in ["red", "blue", "green",'orange']:
    crush.color(c)
    crush.forward(100)
    crush.left(90)
wn.exitonclick()
wn.mainloop()
