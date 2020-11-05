
def create_bow(rawtext):
    stopwords = [x for x in open("stopwords.txt").read().split()]
    
    dict = {}
    rawtext = rawtext.lower()
    text = ""
    for letter in rawtext:
        if letter.isalpha() or letter == '\n' or letter == ' ':
            text = text + letter
    for word in text.split():
        if word not in stopwords:
            dict.setdefault(word,0)
            dict[word] = dict[word] + 1
    return dict


def file_to_bow(filename):
    f = open(filename)
    text = f.read()
    d = create_bow(text)
    return d

# Example
# find all the words (and counts) that appear more than twice
#[(word, d[word]) for word in d.keys() if d[word] > 2]

def getword(bag,morethan):
    return [(word, bag[word]) for word in bag.keys() if bag[word] > morethan]
