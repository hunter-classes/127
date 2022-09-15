def is_even(n):
    if n%2 == 0:
        return True
    else:
        return False	

def is_even_short_version(n):
    return n%2 == 0


def is_odd(n):
    pass

result = is_even(10)
print("Result for 10 is:",result)
result = is_even(11)    
print("Result for 11 is:",result)

print("Direct call:",is_even(11))

print("Direct call short version:",is_even_short_version(15))
print("Direct call short version:",is_even_short_version(16))
