import math

############### question 1 #######################
#
def f(n,k):
    numerator = (1+n)**k
    denomiator = math.sqrt(k+1)
    return numerator / denomiator

############### question 2 #######################
#
def remove_e(sentence):
    result = ""
    for letter in sentence:
        if letter != 'e':
            result = result + letter
    return result

############### question 3 #######################
#
def box(length,height):
    result = ""
    if height % 2 != 0:
        height = height - 1;
    xs = "X"*length
    os = "O"*length
    for row in range(height // 2):
        result = result + os+'\n'
        result = result + xs+'\n'
    return result    
        
############### question 4 #######################
#
def makeacronym(w):
    acronym = ""
    w = w.lower()
    for word in w.split():
        acronym = acronym + word[0]
    return acronym


print("-------------- Question 1 -----------------")
ans = f(5,6)
print("n=5, k=6",ans)
print()
print("-------------- Question 2 -----------------")
s = "The letter E will be removed"
print("original: ",s)
print("result: ",remove_e(s))
print()
print("-------------- Question 3 -----------------")
print("l=5,h=5")
print(box(5,5))
print()
print("l=10,h=6")
print(box(10,6))
print("-------------- Question 4 -----------------")
s = "Laugh out loud"
print(s," : ", makeacronym(s))
print()
s = "In my humble opinion"
print(s," : ", makeacronym(s))
print()
      
