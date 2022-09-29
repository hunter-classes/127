
def fizzbuzz(n):
#    number = 1
#    while number < n:
#        print(number)
#        number = number + 1
    for number in range(1,n):
        if number % 3 == 0 and number % 5 == 0:
            print("fizzbuzz")
        elif number % 3 == 0:
            print("fizz")
        elif number % 5 == 0:
            print("buzz")
        else:
            print(number)
        

value = 20
print("Fizzbuzz up to ",value)
fizzbuzz(value)
