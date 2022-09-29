
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
        

def fizzbuzz2(n):
    
    for number in range(1,n):
        output = ""
        if number % 3 == 0:
            output = output + "fizz"
        if number % 5 == 0:
            output = output + "buzz"
        if output == "":
            output = str(number)
        print(output)
        
value = 20
print("Fizzbuzz up to ",value)
fizzbuzz2(value)
