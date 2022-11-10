
s="""this is a string with a bunch of lower case letters. There's nothing too
interesting about it other than the fact that there are a bunch
of words over multiple lines and we're going to do some processing on them
"""

translations = """a:b
c:d
oldword:neword
"""

def count_letters(s):
    """
    Count the number of times each letter
    appears in s
    """
    counts = {}
    for letter in s:
        if letter in counts.keys():
            counts[letter] = counts[letter] + 1
        else:
            counts[letter]=1
    return counts


def count_words(s):
    counts = {}
    for word in s.split():
        counts.setdefault(word,0)
        counts[word] = counts[word]+1
        
    return counts

letter_counts = count_letters(s)
word_counts = count_words(s)
