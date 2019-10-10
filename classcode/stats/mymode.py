import random

def build_list(l,max_value):
    result = []
    for i in range(l):
        result.append(random.randrange(max_value))
    return result

def frequency(l,i):
    count = 0
    for item in l:
        if item==i:
            count = count + 1
    return count

def mymode(l):
    mode_so_far = l[0]
    freq_so_far = frequency(l,mode_so_far)
    for item in l:
        freq_item = frequency(l,item)
        if freq_item > freq_so_far:
            mode_so_far = item
            freq_so_far = freq_item
    return mode_so_far


        

