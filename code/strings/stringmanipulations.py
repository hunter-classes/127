def initialize(name):
    """
    input: a string in the form "first last"
    returns: a string in the form "F. Last"
    """
    result = ""
    # isolate, uppercase and add first init to result
    first = name[0]
    first = first.upper()
    result = result + first + "."

    # find the last name (after space), cap it and add to result
    location = name.find(' ')
    last = name[location+1:].capitalize()
    result = result + ' ' + last
    return result
    
    
def bondify(name):
    """
    input: a string in the form "first last"
    returns: a string in the form "Last, First Last"
    """
    
# Test initialize
result = initialize("james bond")
print("james bond --> ",result)


# Test Bondify
