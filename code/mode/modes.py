import random

def findLargest(dataset):
    largeSoFar = dataset[0]
    for item in dataset[1:]:
        if item > largeSoFar:
            largeSoFar = item
    return largeSoFar



def freq(dataset,v):
    count = 0
    for item in dataset:
        if item == v:
            count = count + 1
    return count


def buildRandomList(size,maxvalue):
    #result = []
    #for x in range(size):
    #    result.append(random.randrange(maxvalue))
    #return result
    result = [random.randrange(maxvalue) for x in range(size)]
    return result 
                      
dataset = buildRandomList(20,30)
