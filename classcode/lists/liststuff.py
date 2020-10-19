import random

# lists
color_list = ['red','green','blue']
# strings are immutable
s="abcde"
# can't say s[2] = 'x'

sample_list=[1,2,3,4,5]
# strings are mutable - they can be changed directly
print(sample_list)
sample_list[2]=100
print(sample_list)
sanple_list2 = [1,2,'hello world',3.5,True,5]

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
    smallest = l[0]
    for i in range(len(l)):
        if l[i] < smallest:
            smallest=l[i]
    return smallest

def freq(l,item):
    """
    returns the number of times item appears
    in list l
    """
    count = 0;
    for i in l:
        if i == item:
            count = count + 1
    return count

l=[1,2,3,4,5]
l2 = [1,2,3,4,5]
l3 = l # l3 refers to the same blocks of memory
       # as l does
       
l4 = l2[:] # this makes a copy of the data in l2
           # so l4 is not an alias of l2 (whereras
           # l3 is an alias for l
           # but rather l4 is a new list with new data
           

