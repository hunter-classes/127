


def fizzbuzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return "fizzbuzz"
    elif number % 3 == 0:
        return "fizz"
    elif number % 5 == 0:
        return "buzz"
    return number

def fizzbuzzrunner(max):
    for i in range(1,max + 1):
        print(i,fizzbuzz(i))
    

def fizzbuzzwhilerunner(max):
    i = 1
    while i <= max:
        print(i,fizzbuzz(i))
        i=i+1
    

