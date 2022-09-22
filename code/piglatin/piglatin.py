def piglatinify(word):
    
    first = word[0]
    if first == 'a' or first == 'e' or first == 'i' \
               or first == 'o' or first == 'u':
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
