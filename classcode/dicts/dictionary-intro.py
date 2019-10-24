
l=[] # empty list
#d={} # empty dictionary
d = {'first' : "sam", "last" : "Spade"}
l.append(2)
l.append(20)
person={}
person['first'] = "Sam"
person['last'] = "Spade"

print(person['last'])
person['numbers'] = [1, 2, 3, 4, 5]

l.append(person)
person['lastagain'] = "Spade"

person[1]="this has a number key"
person[20]=10.23

sample_dict = {4:"four",5:'five',1:'one',2:'two',3:'three'}
d2 = {'one':100,'two':200,'three':300,
      'four':400,'five':500,'secondfive':500}

#for item in d2:
#    print("d2[" + item + "] : " + str(d2[item]))
# 200 in d2
# "two" in d2
# "two" in d2.keys()
# 200 in d2.values()

flipped = {}
for k,v in d2.items():
    flipped[v] = k
 

counts = {'pizza':10,'chocolate':9,'chocolate pizza':10}
foodlist = ['pizza','chocolate','chocolate pizza','cheese']

for food in foodlist:
    if food in counts:
        print(food + " : " + str(counts[food]))
    else:
        print(food + " :  0")

print("\n\n")

for food in foodlist:
    counts.setdefault(food,0)
    print(food + " : " + str(counts[food]))
