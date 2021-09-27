# DON'T DO THS--> from random import *
# THIS is a bit better--> from random import randrange,randint

#these two options are the way to go
import random
# now we use random. to use it. ex random.randrange(5,50)

# This is an alternative if the name is really long
# import random as rnd

# the above lets us use rnd as a shorthand for random
# so we can write rnd.randrange(5,50) etc.

import piglatin as pl


def main():
    test_sentence="love struck romeo art of serenade"
    output = ""
    for word in test_sentence.split():
        result = pl.piglatinify(word)
        output = output + result + " "
    output = output.rstrip(" ")
    print(output)
    


def listExample():
    l=[5,2,3,10,15,30,23,3,30,50,3]
    print(l)
    z = 0
    for item in l:
        if item == 3:
            z=z+1
    print(z)

    
    for i in range(len(l)):
        l[i] = l[i] + 1
        
    print(l)
        
if __name__ == "__main__":
    listExample()
    


