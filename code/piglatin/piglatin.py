# TODO:
# 1. Make it work for capitalized words
#    ex: Cable -> Ablecay
# 2. Handle periods (and possibly other punctuation)
#    ex: Able. -> Ableay.
#        cable. -> ablecay.


def piglatinify_v1(word):
    
    first = word[0]
    if first in 'aeiouAEIOU':
        result = word + 'ay'
    else:
        if first == first.upper():
            result = word[1:].capitalize()+first.lower()+'ay'
        else:
            result = word[1:]+first+'ay'
    
    return result


def piglatinify(word):

    if word[-1] in ".!?":
        end_of_sent = True
        punctuation = word[-1]
        word = word[:-1]
    else:
        end_of_sent = False

    # keep track of if the word had a capital letter
    if word[0] == word[0].upper():
        capital = True
    else:
        capital = False
    
    # transform to lower case
    word = word[0].lower()+word[1:]
    first = word[0]

    # turn into piglatin
    if first in 'aeiou':
        result = word + 'ay'
    else:
        result = word[1:]+first+'ay'
    
    # if we started with a capital letter we
    # have to transform the result back to have
    # a capital letter
    if capital:
        result = result.capitalize()
    
    # test to see if we have to add punctuation on at the end
    if end_of_sent:
        result = result + punctuation
    return result
