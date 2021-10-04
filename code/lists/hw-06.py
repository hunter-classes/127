import random

def build_random_list(size,minval,maxval):
    l = []
    for i in range(size):
        l.append(random.randrange(minval,maxval))
    return l

def find_min(l):
    if (len(l)<1):
        return None
    smallest_so_far = l[0]
    for item in l:
        if item < smallest_so_far:
            smallest_so_far = item
    return smallest_so_far

def combine(l1,l2):
    len1 = len(l1)
    len2 = len(l2)
    if len1 < len2:
        shorter = len1
    else:
        shorter = len2
    result = []
    i = 0
    while i < shorter:
        result.append(l1[i] + l2[i])
        i = i + 1
    if shorter == len1:
        result = result + l2[i:]
    else:
        result = result + l1[i:]
    return result
        
def list_sum(l):
    sum = 0
    for item in l:
        sum = sum + item
    return sum


def sub_sum(l):
    result = []
    for item in l:
        result.append(list_sum(item))
    return result

