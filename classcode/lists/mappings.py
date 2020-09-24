
def keep_ods(l):
    """
    return a list with only the odd numbers
    """
    result = []
    for item in l:
        if item%2==1:
            result.append(item)
    return result


def is_odd(x):
    """
    returns true if a number is odd and false otherwise
    """
    return x%2==1

def is_even(x):
    """
    returns true if a number is odd and false otherwise
    """
    return not(is_odd(x))

def is_more_than_five(x):
    return x>5

def is_more_five_even(x):
    return is_more_than_five(x) and is_even(x)

def filter(fun,l):
    """
    return a list with only the odd numbers
    """
    result = []
    for item in l:
        if fun(item):
            result.append(item)
    return result


def cap1(l):
    """
    CHANGE all the items in the list so that each word
    is capitalized

    This function is NOT pure - it has a side effect - it changes
    the values in the list
    """
    for i in range(len(l)-1):
        l[i] = l[i].capitalize()

def cap2(l):
    """
    This version does not work.

    """
    for item in l:
        # since item is a seprate variable, when you assigne item to be the
        # capitalization of item, you're just assigning it to the variable
        # item and not in the list
        item = item.capitalize()

def cap3(l):
    """
    returns a new list where the values are the capitalized versions of the
    corresponding values of the old list

    This is a pure function. It takes something and returns something new 
    and it doesn't change anything (has no side effects)

    pure functions are preferred - easier to design, debug, reason about
    """
    result = []
    for item in l:
        result.append(item.capitalize())
    return result
        

def squarelist(l):
    result = []
    for item in l:
        result.append(item*item)
    return result


def map(fun,l):
    result = []
    for item in l:
        result.append(fun(item))
    return result

def cap_word(w):
    return w.capitalize()

def square(x):
    return x*x

def cube(x):
    return x*x*x


wordlist = ['cat','dog','frog','iguana']


