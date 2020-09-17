
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

def piglatinify_sentence(sentence):
    """
    convert an entire sentence into piglatin
    and return the new sentence.
    
    make sure to handle periods
    """

    word_list = sentence.split()
    if word[-1] == '.':
        hasPeriod = True
    else:
        hasPeriod = False
        
    result = ""
    for word in word_list:
        pigword = piglatinify(word)
        result = result + pigword + " "
    return result[0:-1]


answer = piglatinify("hello")
print(answer)

sentence = "No TV and no beer makes Homer something something."
# something. ---> omethingsay. (, ; : could be handled similarly)
#

answer = piglatinify_sentence(sentence)
print(answer)
