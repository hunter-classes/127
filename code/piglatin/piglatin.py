import random 
def piglatinify(word):
    """
    input: a single word
    returns: the word transformed into piglatin

    Notes: if the first letter is a vowel, add "ay" to end
           otherwise move first to end and  add "ay" to end
    """

    # check for empty input
    if word=="":
        return word
    
    # separate word into first and rest
    first = word[0]
    rest = word[1:]

    VOWELS = 'aeiouAEIOU'
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
    word1 = piglatinify("hello")
    word2 = piglatinify("world")
    result = word1 + " " + word2
    print(result)

if __name__=="__main__":
    tests()
    
