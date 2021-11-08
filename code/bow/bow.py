
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

    # find the largest

    # find the words that occur that number of times

    #return them
    pass

def main():
    load_bow("chapter1.txt")

if __name__=="__main__":
    main()
    
