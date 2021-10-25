import random
import time

def frequencies(l,value):
    count = 0;
    for item in l:
        if item == value:
            count = count + 1
    return count


def mode1(L):
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

def mode2(L):
    mode_so_far = L[0]
    count_so_far = L.count(mode_so_far)
    
    for value in L:
        count_value = L.count(value)
        if count_value > count_so_far:
            count_so_far = count_value
            mode_so_far = value

    return mode_so_far

def modefast(L):
    # first make a list to hold the tallies
    # since our data values are between 0 and 99 inclusive
    # we need a list of 100 spaces (0 through 99)
    tallies = [0] * 100

    # alternate ways to do the previous line:
    # tallies = [0 for x in range(100)]
    # or
    # tallies = []
    # for i in range(100):
    #   tallies.append(0)

    # second, go through L and add to the tallies
    for item in L:
        tallies[item] = tallies[item] + 1

    # finally, find the index of the largest entry
    # in tallies
    largeindexsofar = 0
    for i in range(len(tallies)):
        if (tallies[i] > tallies[largeindexsofar]):
            largeindexsofar = i
    # largeindexsofar has the mode
    return largeindexsofar

def sumeven(l):
    s = 0
    for item in l:
        if item % 2 == 0:
            s = s + item
    return s

def twoloopssequential(l):
    s = 0
    for item in l:
        if item % 2 == 0:
            s = s + item
    for item in l:
        if item % 2 != 0:
            s = s + item
    return s

def speedtest(size,func):
    l=[random.randrange(100) for x in range(size)]
    start_time = int(time.time()*1000)
    m = func(l)
    elapsed_time = int(time.time()*1000) - start_time
    return elapsed_time

    


def main():
    pass

if __name__=="__main__":
    main()
    
