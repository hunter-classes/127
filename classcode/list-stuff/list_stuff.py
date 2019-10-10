import random

def freqency(x,l):
    """
    return the number of times item occurs in list l
    """
    count = 0
    if item == x:
            count = count + 1
    return count


def find_largest(l):
    """
    inputs: a list of numbers
    returns: the largest values
    >>> find_largest([5,3,2,6,10,1,3])
    10
    >>> find_largest([2,2,2,2,2,10,10,10,11,11,11])
    11
    """
    largest = l[0]
    for item in l:
        if item > largest:
            largest = item
    return largest

def find_largest_index(l):
    largest_index = 0
    for i in range(len(l)):
        if l[i] > l[largest_index]:
            largest_index = i
    return largest_index




def make_random_list(num_items,max_size):
    result = []
    for i in range(num_items):
        result.append(random.randrange(max_size))
    return result

l = make_random_list(20,20)


def mode(l):
    """
    Return the value of the  mode (most frequent value) from list l
    assume that there is only one mode (if there are multiple modes
    you can return any of them)

    >>> mode([5,4,2,6,2,9,6,8,6,10])
    6
    >>> mode([1,2,3,4,5,4,6,7,5,10,11,12])
    4
    >>> mode([1,2,3,4,5,6,7,8])
    1
    """
    pass
