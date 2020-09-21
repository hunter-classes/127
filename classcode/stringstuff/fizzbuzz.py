def fizzbuzz(n):
    """
    print out the fizzbuzz test
    return nothing
    """
    for i in range(1,n):
        if i % 3 == 0 and i % 5 == 0:
            print('fizzbuzz')
        elif i % 3 == 0:
            print('fizz')
        elif i % 5 == 0:
            print('buzz')
        else:
            print(i)
                    
        
        
def add1(x):
    return x+1

def add1_bad(x):
    print(x+1)
    


       
       
def main():
    # print(fizzbuzz(16)) <- we don't want to print
    # the return value here since the routine
    # is explicitly supposed to print and return None
    fizzbuzz(16)
    



if __name__=='__main__':
    main()
    
