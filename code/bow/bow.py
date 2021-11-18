
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

        

def sentiment_total_words(bag,wordlistfile):
    # first, read in wordlistfile into a list
    sentwords = open(wordlistfile,encoding="Latin-1").read().split()

    # Version 1: calculate the total number of words in bag
    total_words = count_words(bag)
    
    # Version 1: Calculate the number of words in bag that
    #            are in wordlistfile
    # sum = 0
    # for k in bag.keys():
    #     if k in sentwords:
    #        sum = sum + bag[k]

    # shorter list comprehension version 
    total_sentwords = sum([bag[k] for k in bag.keys() if k in sentwords])        
    # Version 1: return the number from wordlistfile / total words
    return total_sentwords / total_words


def sentiment_unique_words(bag,wordlistfile):
    # first, read in wordlistfile into a list
    sentwords = open(wordlistfile,encoding="Latin-1").read().split()

    # Version 1: calculate the total number of words in bag
    # Version 2: calculate the # of different words in bag 
    total_words = len(bag.keys())
    
    # Version 2: Calculate the number of different words in bag
    #            that are in wordlistfile
    # sum = 0
    # for k in bag.keys():
    #      if k in sentwords:
    #         sum = sum + 1
    total_sentwords = sum([1 for k in bag.keys() if k in sentwords])        

    # Version 2: return the same ration but with the V2 numbers
    return total_sentwords / total_words    
    

onebag = load_bow("one.dat")
onebag_s = remove_stop_words(onebag,"stopwords.txt")

twobag = load_bow("two.dat")
twobag_s = remove_stop_words(twobag,"stopwords.txt")


one_pos_tot = sentiment_total_words(onebag,"positives.txt")
one_pos_s_tot = sentiment_total_words(onebag_s,"positives.txt")
one_neg_tot = sentiment_total_words(onebag,"negatives.txt")
one_neg_s_tot = sentiment_total_words(onebag_s,"negatives.txt")


two_pos_tot = sentiment_total_words(twobag,"positives.txt")
two_pos_s_tot = sentiment_total_words(twobag_s,'positives.txt')
two_neg_tot = sentiment_total_words(twobag,"negatives.txt")
two_neg_s_tot = sentiment_total_words(twobag_s,"negatives.txt")


one_pos_unique = sentiment_unique_words(onebag,"positives.txt")
one_pos_s_unique = sentiment_unique_words(onebag_s,"positives.txt")
one_neg_unique = sentiment_unique_words(onebag,"negatives.txt")
one_neg_s_unique = sentiment_unique_words(onebag_s,"negatives.txt")


two_pos_unique = sentiment_unique_words(twobag,"positives.txt")
two_pos_s_unique = sentiment_unique_words(twobag_s,'positives.txt')
two_neg_unique = sentiment_unique_words(twobag,"negatives.txt")
two_neg_s_unique = sentiment_unique_words(twobag_s,"negatives.txt")

print("ONE:")
print("Positive total: ",one_pos_s_tot)
print("Negative total: ",one_neg_s_tot)
print()

print("TWO:")
print("Positive total: ",two_pos_s_tot)
print("Negative total: ",two_neg_s_tot)
print()
print()


print("ONE:")
print("Positive unique: ",one_pos_s_unique)
print("Negative unique: ",one_neg_s_unique)
print()

print("TWO:")
print("Positive unique: ",two_pos_s_unique)
print("Negative unique: ",two_neg_s_unique)
print()

