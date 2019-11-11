
# open the file
f = open("mobydick.txt")

# read the entire text into a big string
#all = f.read()
# split into words on whitespace
#words = all.split()

# split into lines
#lines = all.split("\n")
# split a particular line into words
#w = lines[2].split()

# split directly into lines
#lines = f.readlines()

all = f.read()
cleaned = all.lower()
#for letter_to_remove in ",.;:!?-_0123456789":
#    cleaned = cleaned.replace(letter_to_remove,' ')

letters_to_remove = ',.;:!?-_0123456789'
cleaned = [ x for x in cleaned if x not in letters_to_remove]
cleaned = "".join(cleaned)


# word_counts = {}
# for word in cleaned.split():
#     word_counts.setdefault(word,0)
#     word_counts [word] = word_counts[word] + 1

word_counts = {}
wordlist = cleaned.split()
for index in range(len(wordlist)):
    word = wordlist[index]
    word_counts.setdefault(word,0)
    word_counts[word] = word_counts[word] + 1

values = word_counts.values()
values.sort()

over50 = [(word,word_counts[word]) \
          for word in word_counts \
          if word_counts[word] > 50]

from20to50 = []
for word in word_counts:
    if word_counts[word] >= 20 and word_counts[word] <= 50:
        from20to50.append( (word,word_counts[word]))
        
from10to20 = [(word,word_counts[word]) \
              for word in word_counts \
              if word_counts[word] > 10 and word_counts[word] < 20]

u10 = [(word,word_counts[word]) \
              for word in word_counts \
              if word_counts[word] <10]

