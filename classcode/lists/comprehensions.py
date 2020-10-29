import random

def build_random_list(length, min, max):
    l=[]
    for i in range(length):
        l.append(random.randrange(min,max))
    return l

rlist = build_random_list(20,0,10)

oddlist = []
for item in rlist:
    if item % 2 == 1:
        oddlist.append(item)



ups=[]
for word in words:
    ups.append(word.upper())

odds = [x for x in range(1,40,2)]

l = [x*x for x in range(5)]

l = [ 5 for x in range(10)]

l = ["HELLO" for x in range(5)]

words = ["cat","dog","running","caligraphy"]
ups = [ word.upper() for word in words]

numbers = [random.randrange(0,1000) for x in range(20)]

odds = [x for x in range(40) if x%2==1]

smalls = [ n for n in numbers if n < 200]

lc = [word for word in words if(len(word) >= 3 and len(word) < 8)]


grades = [ [90,95,100], [80,90,92], [100,50], [88,89,99,95]]
avgs = [ sum(studentgrades)/len(studentgrades) for studentgrades in grades]

longgrades = [
    {'name':'john', 'grades':[90,99,93]},
    {'name':'susan','grades':[100,98,96]}
]


longaverages = [
    {'name':s['name'],
     'grades' : s['grades'],
     'average' : sum(s['grades'])/len(s['grades'])
     }
    for s in longgrades
]

colors = ['red','green','blue']
foods = ['pizza', 'hamburger', 'cake', 'eggs']

food_colors = [ [f,c] for f in foods for c in colors]
food_colors2 = [ [f,c] for f in foods for c in colors if c != 'red']

w = [f+":"+c for c in colors for f in foods if len(f+":"+c)>10]
