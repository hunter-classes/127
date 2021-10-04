import random

# this version is PURE
# it doesn't change anything
# it makes a new list and returns s
def build_random_list(size,minval,maxval):
    l = []
    for i in range(size):
        l.append(random.randrange(minval,maxval))
    return l

def square_list1(l):
    result = []
    for item in l:
        result.append(item*item)
    return result 

# this version is NOT pure
# it has a side effect - l itself is modified
# note that it does NOT return anythin
def square_list2(l):
    for index in range(len(l)):
        l[index] = l[index] * l[index]

# This is also NOT pure but it returns the list so
# you CAN reassign it if you want
# like l = square_list3(l)
def square_list3(l):
    for index in range(len(l)):
        l[index] = l[index] * l[index]
    return l




def cap_words(l):
    result = []
    for word in l:
        first = word[0]
        rest = word[1:]
        result.append(first.upper()+rest)
    return result

def find_min(l):
    pass
