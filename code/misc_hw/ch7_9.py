
def isEven(number):
    if number % 2 == 0:
        return True
    else:
        return False

def isEvenTerse(number):
    return number % 2 == 0

def isOdd(number):
    return not isEven(number)

longString ="""
Street bands have been picking up the slack for the last year in NYC, performing for outside diners and more throughout the city. This festival celebrates them and puts them front and center.

Email readers can see the video 
"""
def countLetters(s,letter):
    """ 
    count the number of times letter occurs in string s
    """
    count = 0
    for l in s:
        print(l)


longString ="""
Street bands have been picking up the slack for the last year in NYC, performing for outside diners and more throughout the city. This festival celebrates them and puts them front and center.

Email readers can see the video 
"""
def countLetters(s,letter):
    """ 
    count the number of times letter occurs in string s
    """
    count = 0
    print(s)
    for l in s:
        if l==letter.lower() or l==letter.upper():
            count = count + 1
    return count 


def tests():
    print("IsEven tests")
    print("isEven(23)",isEven(23))
    print("isEven(24)",isEven(24))
    print()
    print("IsEvenTerse tests")
    print("isEvenTerse(23)",isEvenTerse(23))
    print("isEvenTerse(24)",isEvenTerse(24))
    print()
    print("IsOdd tests")
    print("isOdd(23)",isOdd(23))
    print("isOdd(24)",isOdd(24))
    print()
    print("Count letters a in longString")
    print(countLetters(longString,'A'))

if __name__=="__main__":
    # put the stuff here to be run automatically if you
    # run this file as a program 
    tests()
    
