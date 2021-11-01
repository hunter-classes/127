import random

def find_max(l):
    m = l[0]
    for item in l:
        if item > m:
            m = item
    return m




def build_word_lengths(text):
    lengths = {}
    for word in text.split():
        lengths[word] = len(word)
    return lengths

def get_most_longest_word(text):
    counts = build_word_lengths(text)
    vals = counts.values()
    maxval = find_max(list(vals))

    largest_values = [x for x in counts.keys() if counts[x] == maxval]
    return largest_values

text = open("input.txt").read()
result = get_most_longest_word(text)
print(result)

