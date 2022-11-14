
def load_bow(filename):
    bag = {}
    f = open(filename).read()
    for word in f.split():
        word = word.rstrip(".;,?\n")
        word =  word.lower()
        bag.setdefault(word,0)
        bag[word] = bag[word] + 1
    return bag


def find_most_frequent(bag):
    # get all the counts (values) from the bag
    counts = bag.values()
    
    # find the largest
    counts = list(counts)
    counts.sort()
    max = counts[-1]

    # find the words that occur that number of times
    #result = []
    #for word in bag.keys():
    #    if bag[word] == max:
    #        result.append(word)
    result = [x for x in bag.keys() if bag[x] == max]
    #return them
    return result

def get_words_more_frequent(bag,count):
    result = [x for x in bag.keys() if bag[x] >= count]
    return result

def get_words_more_frequent_dict(bag,count):
    result = {}
    for word in bag.keys():
        if bag[word] >= count:
            result[word] = bag[word]
    return result


def remove_stop_words(bag,stopwordfilename):
    # read a list of stopwords from stopwordfilename
    f = open(stopwordfilename)
    stopwords = f.read().split()
    
    newbag = {}
    
    for word in bag.keys():
        if word not in stopwords:
            newbag[word] = bag[word]

    return newbag

def count_words(bag):
    #sum = 0
    #for key in bag.keys():
    #    sum = sum + bag[key]

    # shorter list comprehension version
    return sum([bag[k] for k in bag.keys()])

        

onebag = load_bow("one.dat")
onebag_s = remove_stop_words(onebag,"stopwords.txt")

twobag = load_bow("two.dat")
twobag_s = remove_stop_words(twobag,"stopwords.txt")

