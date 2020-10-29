
def compress(word):
    vowels="aeiouAEIOU"
    result = word[0]
    for letter in word[1:]:
        if letter not in vowels:
            result = result + letter
    return result

def sentence(words):
    result = ""
    for word in words.split():
        result = result + compress(word)+" "
    result = result[:-1]

    return result

def main():
    print(compress("halloween"))
    print(compress("apple"))
    print(compress("Special"))

    print(sentence("I like to eat apple pie"))
    
if __name__=='__main__':
    main()
    
