import random

def freqency(item,l):
    """
    return the number of times item occurs in list l
    """
    pass



def make_random_list(num_items,max_size):
    result = []
    for i in range(num_items):
        result.append(random.randrange(max_size))
    return result

l = make_random_list(20,20)
