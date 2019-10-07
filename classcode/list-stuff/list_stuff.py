import random

def freqency(x,l):
    """
    return the number of times item occurs in list l
    """
    count = 0
    for item in l:
        if item == x:
            count = count + 1
    return count


def find_largest(l):
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
