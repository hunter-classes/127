def is_prime(n):

    if n == 1 or n == 2:
        return True

    for i in range(2,n-1):
        if n % i == 0:
            return False

    # Only prime if it gets through the full loop
    # and never returns false
    return True

def make_acronym(words):
    words = words.lower()
    words = [x for x in words if x in 'abcdefghijklmnopqrstuvwxyz ']
    words = "".join(words)
    result = ""
    for word in words.split():
        result = result + word[0]
    return result


def add_word(dict,word):
    letter = word[0]
    if letter in dict.keys():
        if word not in dict[letter]:
            dict[letter].append(word)
    else:
        dict[letter]=[word]
    return dict


def create_spelling_dictionary(filename):
    d = {}
    f = open(filename)
    for line in f.readlines():
        word = line.strip()
        d = add_word(d, word)
    return d

def lookup(dict,word):
    letter = word[0]
    if letter not in dict.keys():
        return False

    return word in dict[letter]
