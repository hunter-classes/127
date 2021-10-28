# this is an empty dictionary
d = {} 

# we put things in with the [] notation
d['one'] = "hello"
d['two'] = 45
d[3] = ["a","list","of","items"]

# we can see the whole thing
print(d)

# or access using []
print(d['two'])

# you can change things

d['two'] = "New stuff"
d['hello'] = 'world'

print(d)

# and can go through multiple levels
d[3][1]="replaced list with this"
print(d[3])
print(d)

# we can initialize it inline

d2 = {'first' : 'Bugs', 'last' : 'bunny',
      3 : 1945, 'subdict' : {1:2,"a":"b"}, 'sublist' : [1,2,3,4,5]}

# can get all the keys or the values
k = d2.keys()
print(k)

v = d2.values()
print(v)

for key in d2.keys():
    print(key)

for val in d2.values():
    print(val)


# you can delete a key/value pair
del(d['hello'])
