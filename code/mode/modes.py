import random

def frequencies(l,value):
    count = 0;
    for item in l:
        if item == value:
            count = count + 1
    return count


def mode(L):
    # assume the first one is the mode so far
    mode_so_far = L[0]
    count_so_far = frequencies(L,mode_so_far)
    
    # for each item,
    #   count how many times it appears
    #   if it appears more than the mode so far
    #   it becomes the new mode so far
    for value in L:
        count_value = frequencies(L,value)
        if count_value > count_so_far:
            count_so_far = count_value
            mode_so_far = value

    return mode_so_far
def main():
    pass

if __name__=="__main__":
    main()
    
