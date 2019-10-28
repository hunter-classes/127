

def can_make_happy(bugs):
    bugcounts = {}
    for bug in bugs:
        bugcounts.setdefault(bug,0)
        bugcounts[bug] = bugcounts[bug]+1

    # can be happy if there's one space and at least 2 of each:
    if "_" in bugcounts.keys():
        del bugcounts["_"]
        print bugcounts.values()
        return not(1 in bugcounts.values())
    else:
        print("NO SPACE")
        # we have to manually see if the string is already happy
    print(bugcounts)
    


l1 = "ABCCBBABDD_EFGFGG"
print(can_make_happy(l1))

print(can_make_happy("ABCDEFG"))

l1 = "ABCCBBABDD_EFGFEGG"
print(can_make_happy(l1))
