def fb1():
    for i in range(1,100):
        if i % 3 == 0 and i % 5 == 0:
            print(i,"fizzbuzz")
        elif i % 3 == 0:
            print(i,"fizz")
        elif i % 5 == 0:
            print(i,"buzz")
        else:
            print(i)


def fb2():

    for i in range(1,100):
        output = ""
        if i % 3 == 0:
            output = output + "fizz"
        if i % 5 == 0:
            output = output + "buzz"
        if output == "":
            output = i
        print(i,output)

fb2()
