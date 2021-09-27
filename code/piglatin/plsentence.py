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
    print("HELLO")
    print(pl.piglatinify("hello"))
    
if __name__ == "__main__":
    main()
    
