import random 
def piglatinify(word):
    """
    input: a single word
    returns: the word transformed into piglatin

    Notes: if the first letter is a vowel, add "ay" to end
           otherwise move first to end and  add "ay" to end
    """
    # separate word into first and rest
    first = word[0]
    rest = word[1:]

    VOWELS = 'aeiou'
    if first in VOWELS:
        encoded = word + "ay"
    else:
        encoded = rest + first + "ay"
   
    
    return encoded 


def tests():
    s = "hello"
    print(s,piglatinify(s));
    s = "able"
    print(s,piglatinify(s));
    s = "bob"
    print(s,piglatinify(s));
    

if __name__=="__main__":
    tests()
    
