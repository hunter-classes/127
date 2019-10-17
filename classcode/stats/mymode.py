import random

def build_list(l,max_value):
    result = []
    for i in range(l):
        result.append(random.randrange(max_value))
    return result

def frequency(l,i):
    count = 0
    for item in l:
        if item==i:
            count = count + 1
    return count

def largest(l):
    l_so_far = 0
    for item in l:
        if item > l_so_far:
            l_so_far = item
    return l_so_far


def mymode1(l):
    mode_so_far = l[0]
    freq_so_far = frequency(l,mode_so_far)
    for item in l:
        freq_item = frequency(l,item)
        if freq_item > freq_so_far:
            mode_so_far = item
            freq_so_far = freq_item
    return mode_so_far

def mymode2(l):

    
    tallies = []
    for i in range(100):
        tallies.append(0)
        
    for item in l:
        tallies[item] = tallies[item] + 1
        
    # figure out which bucket has the largest value
    largest_index = 0
    for i in range(len(tallies)):
        if tallies[i] > tallies[largest_index]:
            largest_index = i
            
    return largest_index

def bucket_sort(l):
    
    tallies = []
    for i in range(10):
        tallies.append(0)
        
    for item in l:
        tallies[item] = tallies[item] + 1
        
    result = []
    for i in range(len(tallies)):
        for j in range(tallies[i]):
            result.append(i)

    print(tallies)
            
    return result


l = build_list(20,10)
print("GO")
#print(l)
#print("-----")
#print(mymode1(l))
print(l)
print(bucket_sort(l))


