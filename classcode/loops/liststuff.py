import random


l  =['one','two','three']
l2 = [1,2,3]
#print(l)
#print(l2)
l3 = []

def build_random_list(size,minvalue,maxvalue):
    result=[]
    for i in range(size):
        result.append(random.randrange(minvalue,maxvalue))
    return result

