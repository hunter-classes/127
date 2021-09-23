for color in ['red','green','blue']:
    print(color)

colors = ['red','green','blue','purple']
# each time through the loop, c will be assigned the next value
# from the list colors 
for c in colors:
    print(c)
print()
# range(5,10) gives a collection that starts at 5
# and ends at 9 (first number inclusive, last one exclusive)
for number in range(5,10):
    print(number)
print()
# only giving one value to range makes it start at 0
for number in range(10):
    print(number)
print()
# you can also give it a step
for number in range(3,30,5):
    print(number)
print()
s = "Hello World!"
for letter in s:
    print(letter)

result = ""
for letter in s:
    if letter in "AEIOUaeiuo":
        result = result + letter.upper()
    else:
        result = result + letter.lower()
print()
print(s,result)

print()
sentence = "a man a plan a canal panama"
for word in sentence.split():
    print(word)
