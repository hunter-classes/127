
def piglatinify(word):
    """
    word   : a single word
    return : the word converted into piglatin
    
    rules  : starts with a vowel --> append "ay"
             otherwise --> move first to last and append "ay"
    """
    
    if len(word) == 0:
        return word
    
    first = word[0]
    if first in "aeiou":
        result = word + "ay"
    else:
        result = word[1:] + first + "ay"
    return result


def sentence_to_piglatin(sentence):
    rlist = []
    for word in sentence.split():
        new_word = piglatinify(word)
        rlist.append(new_word)
        # rlist = rlist + [new_word] <-- same as line above
    
    return " ".join(rlist)


encoded_sentence = sentence_to_piglatin("this is a test")
print(encoded_sentence+":")
