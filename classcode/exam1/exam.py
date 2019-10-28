import math

def q1(n,k):
    num = (1+n)**k
    den = math.sqrt(k+1)
    return num/den


print("----------------- Q1 ---------------------")
print("n = 4, k = 5")
print(q1(4,5))
print(q1(1,2))


#--------------- Q2 -------------------------
def q2(s):
    result = ""
    for letter in s:
        if letter != 'e':
            result = result + letter
    return result
        
print("----------------- Q2 ---------------------")
s = "Does this have any letter e in the string"
print("Orig: "+s)
print("Without e :"+q2(s))

#--------------- Q3 -------------------------
def q31(length,height):
    result = ""
    if height%2!=0:
        height = height -1 
    for i in range(height):
        if i%2==0:
            result = result + "O"*length
        else:
            result = result + "X"*length
        result = result + "\n";
    return result


def q32(length,height):
    result = ""
    for i in range(height//2):
        result = result + "O"*length + "\n"+"X"*length+"\n"
    return result

print("----------------- Q3 ---------------------")
print("Length = 5 height = 6")
print(q31(5,6))
print("\n")
print("Length = 5 height = 7")
print(q31(5,7))

print("\n\n")
print("Length = 5 height = 6")
print(q32(5,6))
print("\n")
print("Length = 5 height = 7")
print(q32(5,7))

#--------------- Q4 -------------------------
def q4(l1,l2):
    result=[]

    if len(l1) < len(l2):
        shorter = l1
        longer = l2
    else:
        shorter = l2
        longer = l1
    # add corresponding values up to the lenght of the shorter
    for i in range(len(shorter)):
        result.append(shorter[i]+longer[i])
    # add the rest
    #for j in range(i+1,len(longer)):
    #    result.append(longer[j])

    result = result + longer[i+1:]
    
    return result


print("----------------- Q4 ---------------------")
l1 = [100,2,3]
l2 = [10,20,30]
print(l1)
print(l2)
print(q4(l1,l2))
print('\n')

l1 = [1,2,3,4,5]
l2 = [10,20,30]
print(l1)
print(l2)
print(q4(l1,l2))
print('\n')

l1 = [1,2,3]
l2 = [10,20,30,40,50]
print(l1)
print(l2)
print(q4(l1,l2))
print('\n')

