
def isIncreasing(L):
    for i in range(len(L)-1):
        if L[i] >= L[i+1]:
            return False
    return True


def NumConvert(L):
    num = 0
    for digit in L:
        num = 10*num + digit
    return num

def BinConvert(s):
    num = 0
    for digit in s:
        num = 2*num + int(digit)
    return num

################### isIncreasing #####################
print("--------------- isIncreasing ---------------")
L = [1,2,3,4,5]
print(L," : ", isIncreasing(L))
L = [5,10,8,2]
print(L," : ", isIncreasing(L))
L = [2,5,20,30]
print(L," : ", isIncreasing(L))
L = [1,2,3,5,4]
print(L," : ", isIncreasing(L))
print()

################### NumConvert #####################
print("--------------- NumConvert ---------------")
L = [5,4,2,0,1]
print(L," : ", NumConvert(L))
print()
################### BinConvert #####################
print("--------------- BinConvert ---------------")
s = "101"
print(s," : ", BinConvert(s))
s = "1101"
print(s," : ", BinConvert(s))
s = "11111111"
print(s," : ", BinConvert(s))
print()
