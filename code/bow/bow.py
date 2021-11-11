
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

def sentiment(bag,wordlistfile):
    # first, read in wordlistfile into a list

    # Version 1: calculate the total number of words in bag
    # Version 2: calculate the # of different words in bag 
    
    # Version 1: Calculate the number of words in bag that
    #            are in wordlistfile 
    # Version 2: Calculate the number of different words in bag
    #            that are in wordlistfile

    # Version 1: return the number from wordlistfile / total words
    # Version 2: return the same ration but with the V2 numbers
    
    return 0
def main():
    load_bow("chapter1.txt")

if __name__=="__main__":
    main()
    
