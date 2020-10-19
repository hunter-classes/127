import random
import sys

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


def mode(l):
    # This algorithm is n^2 
    # 3,4,2,6,3,2,9,2,10,2,8
    # assume the first item is the mode so far
    # and record how many times it appears
    mode_so_far = l[0]
    mode_so_far_count = freq(l, l[0])
    mode_so_far_index = 0

    for i in range(len(l)):
        f = freq(l,l[i]) # hidden complexity
        if f > mode_so_far_count:
            mode_so_far = l[i]
            mode_so_far_count = f
            mode_so_far_index = i

    return (mode_so_far,mode_so_far_count)


if __name__=='__main__':
    if len(sys.argv) != 4:
        print("Needs 3 args - listsize, minval, maxval")
    else:
        size = int(sys.argv[1])
        minval = int(sys.argv[2])
        maxval = int(sys.argv[3])
        l = build_random_list(size,minval,maxval)

        m = mode(l)
        print(m)


        
