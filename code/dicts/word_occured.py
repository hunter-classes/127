import random

def find_max(l):
    m = l[0]
    for item in l:
        if item > m:
            m = item
    return m




def build_word_counts(text):
    word_counts = {}
    for word in text.split():
        word_counts.setdefault(word,0)
        word_counts[word] = word_counts[word] + 1
    
    return word_counts

#v = letter_counts.values()
#m = find_max(list(v))
#largest_values = [x for x in letter_counts.keys() if letter_counts[x] == m]



text = open("input.txt").read()
counts = build_word_counts(text)
