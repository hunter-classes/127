
def check_password(p):
    retval = ""

    # check for too short
    if len(p) < 3:
        retval = retval + "must have at least 3 characters"
    # check for too long
    if len(p) > 10:
        retval = retval + "must have no more than 10 characters, "
    
    # check for lower
    hasLowerCase=False
    for l in p:
        if l.islower():
            hasLowerCase = True
    if hasLowerCase == False:
        retval = retval + "need at least one lowercase, "

    # check for upper
    hasUpperCase=False
    for l in p:
        if l.isupper():
            hasUpperCase = True
    if hasUpperCase == False:
        retval = retval + "need at least one uppercase, "

    # check for digit
    hasDigitCase=False
    for l in p:
        if l.isdigit():
            hasDigitCase = True
    if hasDigitCase == False:
        retval = retval + "need at least one digit, "

    retval = retval[0:-2]
    if retval=="":
        retval="valid"
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

    
