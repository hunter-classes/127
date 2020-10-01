
def check_password(p):
    retval = ""

    # check for too short
    if len(p) < 3:
        retval = retval + "must have at least 3 characters"
    # check for too long

    # check for lower

    # check for upper

    # check for digit
    
    return retval

def main():
    r = check_password("")
    print("null password: "+r)

    r = check_password("ab")
    print("ab: " + r)

    r = check_password("thisistoolongofapassword")
    print("too long: " + r)

    r = check_password("ABCDE")
    print("No lower no dig:"+r)

    r = check_password("abcde")
    print("No upper no dig:"+r)

    r = check_password("abCDE1")
    print("Valid: "+ r)

if __name__=="__main__":
    main()

    
