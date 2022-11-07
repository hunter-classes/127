
s="""this is a string with a bunch of lower case letters. There's nothing too
interesting about it other than the fact that there are a bunch
of words over multiple lines and we're going to do some processing on them
"""

def count_letters(s):
    """
    Count the number of times each letter
    appears in s
    """
    counts = {}
    for letter in s:
        counts[letter] = counts[letter] + 1

    return counts


result = count_letters(s)
