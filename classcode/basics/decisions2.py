def possesify(word):
    """
    word : a string representing a word
    returns : the word with an ' appended (if it ends with s already)
              or with an 's appended.
              """
    #lastchar = word[ len(word) - 1 ]
    lastchar = word[-1]
    
    # instead we could have: if word.endswith('s')
    
    #if lastchar == 's':
    #    result = word+"'"
    #    
    #if lastchar != 's':
    #    result = word + "'s"
    
    if word.endswith('s'):
        result = word+"'"
    else:
        result = word + "'s"
    
    return result

def possesify2(word):
    # ends in s
    # ends in not s
    #  ends in 's
    if word.endswith("'s") or word.endswith("'"):
        result = word
    elif word.endswith('s'):
        result = word + "'"
    else:
        result = word + "'s"
    return result

print(possesify("John"))
print(possesify("cars"))
print("----------------")
print(possesify2("John"))
print(possesify2("John's"))
print(possesify2("cars"))
print(possesify2("cars'"))
