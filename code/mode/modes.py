import random

def findLargest(dataset):
    largeSoFar = dataset[0]
    for item in dataset[1:]:
        if item > largeSoFar:
            largeSoFar = item
    return largeSoFar



def freq(dataset,v):
    #count = 0
    #for item in dataset:
    #    if item == v:
    #        count = count + 1
    #return count
    return len([x for x in dataset if x == v])

def buildRandomList(size,maxvalue):
    #result = []
    #for x in range(size):
    #    result.append(random.randrange(maxvalue))
    #return result
    result = [random.randrange(maxvalue) for x in range(size)]
    return result 


def mode(dataset):
    """
    Returns a mode of the dataset, that is
    the value that appears most frequently

    if multiple values appear the same # of times and are
    most frequent, return any of them.

    Ex: mode([5,4,5,6,7,8,5,4]) --> 5 since 5 appears the most
    mode([5,5,5,4,4,4,2,2,7,7,8,8,9]) --> return 5 or 4 since
    both of those values appear 3 times which is the most
    """
    pass


dataset = buildRandomList(20,30)
