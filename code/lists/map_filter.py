import piglatin

data = [1,2,3,4,5,6,7,8,10]
word_data = "one two three four five".split()

def sq(x):
    return x*x


def add_one(x):
    return x+1


def maplist(f,l):
    result = []
    for item in l:
        result.append(f(item))
    return result





r = " ".join(maplist(piglatin.piglatinify,word_data))

def isOdd(x):
    return x%2 == 1

def filterlist(f,l):
    result = []
    for item in l:
        if f(item):
            result.append(item)
    return result



