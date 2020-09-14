# stringstuff.py

def initialize(name):
    f = name[0]
    index = name.find(' ')
    last = name[index+1:]
    result = f +". "+last
    return result

def capitalize(name):
    index = name.find(' ')
    first = name[:index]
    last = name[index+1:]
    result = first.capitalize() + " " + last.capitalize()
    return result

def bondify(name):
    index = name.find(' ')
    first = name[:index]
    last = name[index+1:]
    result = last + ", " + first + " " + last
    return result

    

answer = initialize("Mike Zamansky")
print(answer)
answer = capitalize("hello world")
print(answer)
answer = bondify("James Bond")
print(answer)

