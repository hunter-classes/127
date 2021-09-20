
def initialize(name):
    """
    takes a name in the form "First Last" and returns "F. Last"
    ex: initializa("Mike Zamansky") would return "M. Zamansky"
    """
    first = name[0]
    spaceLocation = name.find(' ')
    lastNameStart = spaceLocation + 1
    lastName =  name[lastNameStart:]
    initName = first + ". " + lastName
    return initName # Note that we're returning the value not printing here
    
def capBoth(name):
    """
    takes a name in the form "first last" and returns the  name
    capitalized.
    ex: capBoth("mike zamansky") --> "Mike Zamansky"
    """
    pass

def bondify(name):
    """
    takes a name in the form "first last" and returns 
    "last, first last"
    ex: bondify("James Bond") --> "Bond, James Bond"
    """
    pass

def tests():
    # add tests here
    oldName = "James Sullivan"
    newName = initialize(oldName)
    print(oldName)
    print(newName)



if __name__=="__main__":
    tests()
    
