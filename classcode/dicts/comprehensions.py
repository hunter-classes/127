import random

l1 = [1,2,3,4,5]

a = [x for x in [1,2,3,4,5]]
b = [var for var in range(10)]
c = [a + 5 for a in range(10)]

c = []
for a in [1,5,2,10]:
    c.append(a+5)
    
c2 = [a + 5 for a in [1,5,2,10]]

d = [x**2 for x in [5,2,3]]

d2 = [20 for item in ["one",'two']]

e = [random.randrange(10) for x in range(20)]


e = [x for x in range(20) if x%2 == 0]

numbers = [random.randrange(200) for x in range(100)]
f = [x for x in numbers if x>50 and x<100]

sentence = "this is a sentence"
g = [x.capitalize() for x in sentence]
g2 = [x.capitalize() for x in sentence.split()]


colours = ['red','green','blue']
things = ['horse','car','tree']

ct = [ (x,y) for x in colours for y in things]

x = [ (x,y) for x in range(3) for y in range(10,40,10)]
y = [ x+y  for x in range(3) for y in range(10,40,10)]

deck = [ [c,suit] for c in range(52) for suit in ['hearts','clubs','spades','diamonds'] ]
