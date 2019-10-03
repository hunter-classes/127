def newguess(n,og):
    ng = (og + (n/og))/2
    return ng

def close_enough(a,b,delta):
    return abs(a-b) < delta

def mysqrt_helper(n,og):
    while (not close_enough(og*og,n,0.00001)):
        ng = newguess(n,og)
        og = ng
    return og

def mysqrt(n):
    return mysqrt_helper(n,1)
