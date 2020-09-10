
def newguess(n,oldguess):
    return (oldguess + (n / oldguess)) / 2
    
    
def mysqrt(n):
    guess = n/2
    
    
    #for i in range(10):
    #    guess = newguess(n,guess)
    #    print(guess)
        
    while abs(guess*guess - n) > 0.00000001:
        guess = newguess(n,guess)
        print(guess)
