def avg(l):
    # calculate the sum of the items
    sum = 0
    for item in l:
        sum = sum + item
        
    # divide by the number of items
    average = sum / len(l)
    return average

def sum_of_squares(l):
    sum = 0;
    for item in l:
        sum = sum + item*item
    return sum


grades = [90,95,100,90]
print("grades:",grades)
average=avg(grades)
print("Average:",average)

l = [3,4,5]
print("l:",l)
print("sum of squares:",sum_of_squares(l))