import random

def build_random_list(size,minval,maxval):
    l = []
    for i in range(size):
        l.append(random.randrange(minval,maxval))
    return l

def myreduce(l,func,startValue):
    result = startValue
    for item in l:
        result = func(result,item)
    return result



def mymap(l,func):
    result = []
    for item in l:
        result.append(func(item))
    return result

def square(x):
    return x*x

def addTwo(x):
    return x+2


def myfilter(l,predicate):
    result = []
    for item in l:
        if predicate(item):
            result.append(item)
    return result

def isOdd(x):
    return x%2!=0

def isEven(x):
    return x%2==0
def plus(a,b):
    return a+b
def minus(a,b):
    return a-b
def times(a,b):
    return a*b
def apply(func,var1,var2):
    return func(var1,var2)

def capsent(a,b):
    return a+" "+b.upper()

def piglatinify(word):
    """
    input: a single word
    returns: the word transformed into piglatin

    Notes: if the first letter is a vowel, add "ay" to end
           otherwise move first to end and  add "ay" to end
    """

    # check for empty input
    if word=="":
        return word
    
    # separate word into first and rest
    first = word[0]
    rest = word[1:]

    VOWELS = 'aeiouAEIOU'
    if first in VOWELS:
        encoded = word + "ay"
    else:
        encoded = rest + first + "ay"

    return encoded

def pls(a,b):
    return a+" "+piglatinfy(b)

