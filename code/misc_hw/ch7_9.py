
def isEven(number):
    if number % 2 == 0:
        return True
    else:
        return False

def isEvenTerse(number):
    return number % 2 == 0

def isOdd(number):
    return not isEven(number)

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


if __name__=="__main__":
    # put the stuff here to be run automatically if you
    # run this file as a program 
    tests()
    
