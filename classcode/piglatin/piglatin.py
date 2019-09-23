
def piglatinify(word):
    """
    word   : a single word
    return : the word converted into piglatin
    
    rules  : starts with a vowel --> append "ay"
             otherwise --> move first to last and append "ay"
    """
    
    if len(word) == 0:
        return word
    
    # if there's a period, strip it out and
    # set append_period so that we know to add it back in at the end
    append_period = False
    if word[-1] == '.':
        append_period = True
        word = word[:-1]
        
    capitalize = False
    if word[0].isupper():
        word=word[0].lower() + word[1:]
        capitalize = True
        
    
    first = word[0]
    if first in "aeiou":
        result = word + "ay"
    elif first:
        result = word[1:] + first + "ay"

    # if we stripped out a period at the top, add it back in
    if append_period:
        result = result + "."
    
    if capitalize:
        result = result.capitalize()
    return result


def sentence_to_piglatin(sentence):
    rlist = []
    for word in sentence.split():
        new_word = piglatinify(word)
        rlist.append(new_word)
        # rlist = rlist + [new_word] <-- same as line above
    
    return " ".join(rlist)


encoded_sentence = sentence_to_piglatin("This is a sentence.")
print(encoded_sentence)
