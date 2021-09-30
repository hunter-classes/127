import random

def build_random_list(size,minval,maxval):
    l = []
    for i in range(size):
        l.append(random.randrange(minval,maxval))
    return l

def keep_odds(l):
    result = []
    for number in l:
        if number % 2 != 0:
            result.append(number)
    return result        

def filter_5(l):
    result = []
    for word in l:
        if len(word)==5:
            result.append(word)
    return result        
    

def sum_to_first_even(l):
    sum = 0
    for number in l:
        sum = sum + number
    for number in l:
        if number % 2 == 0:
            sum = sum - number
            return sum
        

def count_words_of_len_5(s):
    word_list = s.split()
    count = 0
    for word in word_list:
        if len(word)==5:
            count = count + 1
    return count

def count_words_to_sam(s):
    word_list = s.split()
    count = 0
    for word in word_list:
        if word=="sam":
            # we could also have returned count here directly
            break # break exists the loop.
            
        count = count + 1
    return count

def cwts2(s):
    word_list = s.split()
    i = word_list.index("sam")
    return i
                  



word_string="hello frog aaaaa ddd ddddd sam grr ertyu 234"
wl = word_string.split()

