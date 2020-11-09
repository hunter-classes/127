
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


def percent_sentiment(sentiment,bag):
    total_words = sum(bag.values())
    sent_words = sum([bag[x] for x in bag if x in sentiment])
    return sent_words / total_words


# Example
# find all the words (and counts) that appear more than twice
#[(word, d[word]) for word in d.keys() if d[word] > 2]

#positives = []
#for word in open("positives.txt").read().split():
#    positives.append(word)

postivies = [x for x in open("positives.txt",encoding="ISO-8859-1").read().split()]
negatives = [x for x in open("negatives.txt",encoding="ISO-8859-1").read().split()]
