# basic / primative types
a = 20
s = "hello" # strings are special they're kindof like lists but not

# lists
# hold multiple things
# are mutable (chageable)
# access via index l[0], l[1] etc
# indexing, slicing, l[0:3]
l = [1,2,3]
l2 = ['a','b']
l3 = ["hello",22, [1,2,3]]


# dictionaries
d = {}
d['one'] = 'some value under the key one'
d['name'] = 'Horatio'
d[0] = [1,2,3]

d2 = {'first':'Horatio',
      'last' : 'Hornblower',
      'occupation' : 'Sea Captain',
      'age' : 32}

d['some dictionary'] = d2

# we can test to see if there's a key in a dict
0 in d.keys()
1 in d.keys()
# or
d.has_key(0)
d.has_key(1)


counting_dict = {}

# if counting_dict.has_key('apple'):
#     counting_dict['apple'] = counting_dict['apple']+1
# else:
#     counting_dict['apple'] = 1

counting_dict.setdefault('apple',0)
counting_dict['apple'] = counting_dict['apple'] + 1

for k in d.keys():
    print(k, d[k])

# in a dictionary the order is unspecified and could change
