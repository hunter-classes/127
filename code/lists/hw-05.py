import random

def build_random_list(size,minval,maxval):
    l = []
    for i in range(size):
        l.append(random.randrange(minval,maxval))
    return l

def keep_odds(l):
    pass

def sum_to_first_even(l):
    pass

def count_words_of_len_5(s):
    word_list = s.split()
    count = 0
    for word in word_list:
        if len(word)==5:
            count = count + 1
    return count

def count_words_to_sam(s):
    pass

word_string="hello frog aaaaa ddd ddddd grr ertyu 234"


