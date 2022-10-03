s="this is a string"
elist = []
l1 = [12,33,15,20,55,102,3,6,62]
l2 = ['one','two','three']
l3 = ['one',2,122.33,'something',23]
l4 = ['one',23,['a','b','c'],5,[10,11,12]]
slice = l1[3:5]
longer_string = s + s
longer_list = l1+l3
# s[5] = 'I' <-- can't do this - strings are immutable
# we have to do this:
new_string = s[:5]+'I'+s[6:]
# on the other hand, we can change lists directly
l1[4]=9999999

def change_in_place(l,index,new_value):
    l[index]=new_value
print(l1)
change_in_place(l1,4,123)
print(l1)