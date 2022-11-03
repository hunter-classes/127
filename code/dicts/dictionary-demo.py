
d = {}
d[2] = 12345
d[5] = "hello"
d['hello'] = 'world'
d['list']=[2,3,4,5,6]
d[ (1,2) ] = 55
print(d)
d['list']  = 55.3
print(d)

person = {'fist' : "John",
          'last' : "Smith",
          'age' : 50}
person['age'] = person['age'] + 1

print(person)
