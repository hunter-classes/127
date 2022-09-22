# TODO:
# 1. Make it work for capitalized words
#    ex: Cable -> Ablecay
# 2. Handle periods (and possibly other punctuation)
#    ex: Able. -> Ableay.
#        cable. -> ablecay.


def piglatinify(word):
    
    first = word[0]
    if first in 'aeiou':
        result = word + 'ay'
    else:
        # move first letter to end and add 'ay'
        result = word[1:]+first+'ay'
    
    return result


# Testing
test_word = "hello"
result = piglatinify(test_word)
print(test_word," -> ",result)

test_word = "able"
result = piglatinify(test_word)
print(test_word," -> ",result)

test_word = "Cable"
result = piglatinify(test_word)
print(test_word," -> ",result)

test_word = "Able."
result = piglatinify(test_word)
print(test_word," -> ",result)

test_word = "cable."
result = piglatinify(test_word)
print(test_word," -> ",result)
