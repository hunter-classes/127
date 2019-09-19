
s = "aeiou"
l = ['a','e','i','o','u']
t = ('a','e','i','o','u')

print('a' in s)
print('b' in s)
print('a' in l)
print('b' in l)
print('a' in t)
print('b' in t)

print(s[1])
print(l[1])
print(t[1])

print(len(s))
print(len(l))
print(len(t))

# can't do this s[2]='V', instead must to
s = s[0:1] + 'V' + s[2:]
print(s)

l[2]='V'
print(l)


list2 = ['a',230,'Hello World',False, l, 22.33]
print(list2)

for l in "Hello World":
    print(l)
 
print("----------------")
    
for l in [10,20,"hello",30,"world"]:
    print(l)
    
sentence = "Attack each day with an enthusiasm unknown to mankind!"

for letter in sentence:
    print(letter)
    
    
    
print("-------")
for word in sentence.split():
    print(word.upper())
    
    
    