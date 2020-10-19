# add your functions here
def SumOfSquares(l):
    sum = 0
    for value in l:
        sum = sum + value * value
    return sum


def isIncreasling(l):
    for i in range(len(l)-1):
        if l[i]<l[i+1]:
            return True
        elif l[i] > l[i+1]:
            return False

    return true
            


def main():

    print("SumOfSquares:")
    l = [1,2,3]
    result = SumOfSquares(l)
    print(l, result)
    l = [3,1,2]
    result = SumOfSquares(l)
    print(l, result)
    l = [1,2,3]
    result = SumOfSquares([0,-2,2,3])
    print(l, result)
    print("\n\n-------------------\n\n")

if __name__=='__main__':
    main()

    
