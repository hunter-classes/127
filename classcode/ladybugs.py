

def is_happy(bugs):
    """
    the bugs will be happy if all of them have a neighbor of the
    same color
    """
    for i in range(1,len(bugs)-1):
        
        if bugs[i] !='_' and bugs[i] != bugs[i-1] and bugs[i] != bugs[i+1]:
            return False
    return True

def can_be_made_happy(bugs):
    # make sure there are at least 2 bugs of each color
    d = {}
    for bug in bugs:
        if bug != '_':
            d.setdefault(bug,0)
            d[bug] = d[bug] + 1
    counts = d.values()
    if 1 in counts:
        return False # lone bug can't be happy

    # we can be happy if we can rearrange the list - this requires one _
    if '_' in bugs:
        return True

    return is_happy(bugs)



        


bugs = "AABBBCCCDDEE_FF"
bugs2 = "AABCCCDDEE_FF"
