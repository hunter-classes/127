import math

def is_even(n):
    if n%2 == 0:
        return True
    else:
        return False	

def is_even_short_version(n):
    return n%2 == 0


def is_odd(n):
    return not(is_even(n))

def isRightAngle(a,b,c):
    """
    c is longest
    """
    return a*a + b*b == c*c

def isRightAngle2(a,b,c):
    """
    any order for sides
    """
    return isRightAngle(a,b,c) or \
            isRightAngle(b,c,a) or \
            isRightAngle(a,c,b)
            
print("Even tests")
result = is_even(10)
print("Result for 10 is:",result)
result = is_even(11)    
print("Result for 11 is:",result)

print("Odd tests")
result = is_odd(10)
print("Result for 10 is:",result)
result = is_odd(11)    
print("Result for 11 is:",result)

print(isRightAngle(5,3,4))
print(isRightAngle2(5,3,4))

