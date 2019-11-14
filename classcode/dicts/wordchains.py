import random
import sys

def clean_file(filename):
    f = open(filename)
    rawdata = f.read()

    # clean the data
    rawdata = rawdata.lower()
    letters_to_keep = 'abcdefghijklmnopqrstuvwxyz \t\n'
    cleaned = [ x for x in rawdata if x in letters_to_keep]
 
    cleaned = "".join(cleaned)
    return cleaned.split()

def build_wordchain(wordlist,prefix_length):


    d={}

    for i in range(len(wordlist)-prefix_length):
        #prefix or key
        prefix = tuple(wordlist[i:i+prefix_length])

        #suffix or value
        suffix = wordlist[i+prefix_length]

        d.setdefault(prefix,[])
        d[prefix].append(suffix)
    return d


def build_wordchain2(filename):
    f = open(filename)
    rawdata = f.read()

    # clean the data
    rawdata = rawdata.lower()
    letters_to_keep = 'abcdefghijklmnopqrstuvwxyz \t\n'
    cleaned = [ x for x in rawdata if x in letters_to_keep]
 
    cleaned = "".join(cleaned)

    wordlist = cleaned.split()
    d={}

    for i in range(len(wordlist)-2):
        w1 = wordlist[i]
        w2 = wordlist[i+1]
        w3 = wordlist[i+2]
        key = (w1,w2)
        val = w3
        d.setdefault(key,[])
        d[key].append(val)

    return d

def build_wordchain1(filename):
    f = open(filename)
    rawdata = f.read()

    # clean the data
    rawdata = rawdata.lower()
    letters_to_remove = ',.;:!?-_0123456789'
    cleaned = [ x for x in rawdata if x not in letters_to_remove]
 
    cleaned = "".join(cleaned)

    wordlist = cleaned.split()
    d={}

    for i in range(len(wordlist)-1):
        current_word  = wordlist[i]
        next_word = wordlist[i+1]
        d.setdefault(current_word,[])
        d[current_word].append(next_word)

    return d

def generate(d,numwords,startprefix):
    prefix = tuple(startprefix)
    prefixlength = len(prefix)
    result = list(prefix)
    for i in range(numwords):
        try:
            nextword = random.choice(d[prefix])
            result.append(nextword)
        except:
            return " ".join(result)
        # build the next prefix
        prefix = prefix[1:] + (nextword,)

    story = " ".join(result)
    return story


# def generate(d,numwords,startword):
#     word = startword
#     result = [word]
#     for i in range(numwords):
#         nextword = random.choice(d[word])
#         result.append(nextword)
#         word = nextword
#     story = " ".join(result)
#     return story

def build_and_generate(filename,prefixlength,storylength):
    wordlist = clean_file(filename)
    words = build_wordchain(wordlist,prefixlength)
    storystart = wordlist[:prefixlength]
    story = generate(words,storylength,storystart)
    return story

story = build_and_generate("psalms.txt", 3, 50)
print(story)
#words = build_wordchain("testset.txt",1)
#words = build_wordchain2("testset.txt")
#words = build_wordchain("psalms.txt")



# tuple_dict = { ("when","shall") : ["we"],
#                ("shall","we") : ["meet"],
#                ("we","meet") : ["again"],
#                ("meet","again") : ["in"]}
# twl = "we meet happily".split()
# k = (twl[0],twl[1])
# v = twl[2]
# tuple_dict[k].append(v)

# for k in tuple_dict:
#     #w1 = k[0]
#     #w2 = k[1]
#     (w1,w2) = k
#     v = tuple_dict[k]
#     print(w1,w2,v)
    
