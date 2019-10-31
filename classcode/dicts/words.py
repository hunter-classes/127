
# open the file
f = open("chapter1.txt")

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
for letter_to_remove in ",.;!?-_0123456789":
    cleaned = cleaned.replace(letter_to_remove,'')

word_counts = {}
for word in cleaned.split():
    word_counts.setdefault(word,0)
    word_counts [word] = word_counts[word] + 1
    
