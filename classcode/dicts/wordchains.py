

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

#result = build_wordchain("testset.txt")
words = build_wordchain("cyrano.txt")

for k in words:
    print(k,words[k])

