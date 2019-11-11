import random

def build_wordchain(filename):
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

def generate(d,numwords,startword):
    word = startword
    result = [word]
    for i in range(numwords):
        nextword = random.choice(d[word])
        result.append(nextword)
        word = nextword
    story = " ".join(result)
    return story

#result = build_wordchain("testset.txt")
words = build_wordchain("psalms.txt")

tuple_dict = { ("when","shall") : ["we"],
               ("shall","we") : ["meet"],
               ("we","meet") : ["again"],
               ("meet","again") : ["in"]}
twl = "we meet happily".split()
k = (twl[0],twl[1])
v = twl[2]
tuple_dict[k].append(v)

for k in tuple_dict:
    #w1 = k[0]
    #w2 = k[1]
    (w1,w2) = k
    v = tuple_dict[k]
    print(w1,w2,v)
    
