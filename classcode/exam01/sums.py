# add your functions here
def SumOfSquares(l):
    sum = 0
    for value in l:
        sum = sum + value * value
    return sum


def isIncreasing(l):
    for i in range(len(l)-1):
        if l[i] >= l[i+1]:
            return False
    return True
            

def removeSmallest(l):
    smallest = l[0]
    for i in l:
        if i < smallest:
            smallest = i

    result = []

    for i in l:
        if i != smallest:
            result = result + [i]
    return result


    

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

    print("isIncrasing:")
    l = [5,10,15,20]
    print(l,isIncreasing(l))

    l = [5,10,8,20]
    print(l,isIncreasing(l))
    print("\n\n-------------------\n\n")

    print("removeSmallest:")
    print(removeSmallest([5,2,3,1,5,3,5,2,6,1,10]))
    
if __name__=='__main__':
    main()

    
