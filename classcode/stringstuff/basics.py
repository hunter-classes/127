# String Stuff
s1 = "hello world"
s2 = 'hello world'
s3 = "Hello World"
s4 = 'hello world!'

s5 = s1+s2
print(s5)

s1='some new string'

print(s1)
print(s5) # Notice that s5 is not changed when s1 is

# strings are immutable - you can't change them once you
# create them - you have to assign a new one

s6 = s2[0:5] # make a new string with the first 5 chars from s5
s7 = s2[:5] # same as above
s8 = s2[6:] # from 6 to the end
len(s2) # gives you the number of characters in s2


twowords = "hello world"
space_location = twowords.find(' ')
print(twowords, space_location)
first = twowords[:space_location]
print(first)
second = twowords[space_location+1:]
print(second)
