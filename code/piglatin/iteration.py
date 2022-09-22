import random

# this is a foreach loop 
for counter in range(5):
    print(counter)
    
print("--------------")    
# this is a foreach loop 
for counter in [0,1,2,3,4]:
    print(counter)

print("--------------")    
for letter in "this is a sentence":
    print(letter)
print("--------------")    

# while loop
loop_counter = 0
while random.randrange(0,100) < 80:
    print("hello",loop_counter)
    loop_counter = loop_counter + 1
print("The above loop ran this many times: ",loop_counter)
print("--------------")    

# while loop as a counting loop
# first set up a variable to hold the count
i = 0
# then use the boolean to indicate when to stop
while i < 5:
    print(i)
    i = i + 1 # don't forget to change the variale so you eventually stop
    
print("--------------")    
# or count down
i = 5
while i > 0:
    print(i)
    i = i - 1
    

print("--------------")    

# you can also traverse over a string
s  = 'hello world'
i = 0
while i < len(s):
    print(s[i])
    i = i + 1

    