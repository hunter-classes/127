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

def get_most_frequent_word(text):
    counts = build_word_counts(text)
    vals = counts.values()
    maxval = find_max(list(vals))

    largest_values = [x for x in counts.keys() if counts[x] == maxval]
    return largest_values

text = open("input.txt").read()
result = get_most_frequent_word(text)
print(result)

