import random

# lists
color_list = ['red','green','blue']
# strins are immutable
s="abcde"
# can't say s[2] = 'x'

l=[1,2,3,4,5]
# strings are mutable - they can be changed directly
print(l)
l[2]=100
print(l)
l2 = [1,2,'hello world',3.5,True,5]

def build_list(list_length):
    l=[]
    for i in range(list_length):
        l.append(i)
    return l

def build_list_alt(list_length):
    l=[]
    for i in range(list_length):
        l = l + [i]
    return l

def build_random_list(length, min, max):
    l=[]
    for i in range(length):
        l.append(random.randrange(min,max))
    return l


def find_min(l):
    """
    return the value of the smallest item in the list
    assume l is a list of integers
    
    ex: [5,2,8,6,22,10) --> 2
    """
    return None
