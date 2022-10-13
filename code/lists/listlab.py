
def find_smallest(l):
    small_so_far = l[0]
    for item in l[1:]:
        if item < small_so_far:
            small_so_far = item
    return small_so_far

def filter_odd(l):
    result = []
    for item in l:
        if item % 2 == 1:
            result.append(item)
    return result

def cap_sentence(s):
    result_list = []
    for word in s.split():
        result_list = result_list + [word.capitalize()]
    result = " ".join(result_list)
    return result

def long_5_cap(s):
    result_list = []
    for word in s.split():
        if len(word) > 5:
            result_list = result_list + [word.upper()]
        else:
            result_list = result_list + [word]
    result = " ".join(result_list)
    return result

def square_list(l):
    result = []
    for item in l:
        result.append(item*item)
    return result

def combine_sum(l1,l2):
    result = []
    if len(l1) < len(l2):
        shorter = len(l1)
    else:
        shorter = len(l2)
    for i in range(shorter):
        result.append( l1[i]+l2[i] )
    if len(l1) > shorter:
        result = result + l1[i:]
    else:
        result = result + l2[i:]
    return result


def count_len_5(s):
    count = 0
    for word in s.split():
        if len(word) == 5:
            count = count + 1
    return count

def up_to_even(l):
    result = []
    i = 0
    while l[i] % 2 != 0:
        result.append(l[i])
        i=i+1
    return result


def up_to_sam(l):
    result = []
    i = 0
    while l[i] != "sam":
        result.append(l[i])
        i=i+1
    return " ".join(result)


