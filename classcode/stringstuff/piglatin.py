import random

def piglatinify(word):
    """
    Input: a string representing a word
    Returns: a new string of that word in piglatin
    """

    vowels = 'aeiouAEIOU'
    # check the first character of word
    first = word[0]

    if first in vowels:
        result=word+"yay"
    else:
        if first.isupper():
            result = word[1:] + first.lower()+"ay"
            result = result.capitalize()
        else:
            result = word[1:] + first + "ay"
            

    return result
        
result = piglatinify("hello")
print(result)

result = piglatinify("Hello")
print(result)

result = piglatinify("able")
print(result)

result = piglatinify("Able")
print(result)


