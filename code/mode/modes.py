import datetime
import random

def findLargest(dataset):
    largeSoFar = dataset[0]
    for item in dataset[1:]:
        if item > largeSoFar:
            largeSoFar = item
    return largeSoFar



def freq(dataset,v):
    # since this loops over the
    # entire data set once
    # it takes n time 
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

    Strategy:
    assume the first value is the mode
    we can grab its frequency

    for each remaining item in the dataset:
      count that items frequence and see if it's the new
      mode so far    
    """
    modeSoFar = dataset[0]
    freqSoFar = dataset.count(modeSoFar)
    for item in dataset[1:]: #outer loop -> n
        # calling freq each time is n
        # if freq(dataset,item) > freqSoFar:
        if dataset.count(item) > freqSoFar:
            modeSoFar = item
            freqSoFar = dataset.count(item)
    return modeSoFar


def fastMode(dataset):
    # find the largest value in the dataset
    largest = findLargest(dataset)

    # make the buckets for the tallies
    tallies = [0 for x in range(largest+1)]

    # 2. Loop through our dataset and increment the buckets
    for item in dataset:
        tallies[item] = tallies[item] + 1

    # find the bucket with the largest Value
    # - that's the one that occured the most
    mode_count = findLargest(tallies)

    # find and return the index that holds mode_count
    # in tallies
    for i in range(len(tallies)):
        if tallies[i] == mode_count:
            return i

    # we should never actually get here     
    return i

    
    
    
def testMode(size,maxValue):
    print("Dataset Size: ",size)
    dataset = buildRandomList(size,maxValue)
    # print(dataset)
    m = mode(dataset)
    print("Mode: ",m)

def testFindLargest(size,maxValue):
    print("Dataset Size: ",size)
    dataset = buildRandomList(size,maxValue)
    # print(dataset)
    m = findLargest(dataset)
    print("Largest: ",m)

def testFastMode(size,maxValue):
    dataset = buildRandomList(size,maxValue)
    print(dataset)
    result = fastMode(dataset)
    print(result)
#testFindLargest(80000,30)
#testMode(40000,30)

