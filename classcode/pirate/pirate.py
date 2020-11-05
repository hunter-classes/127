import sys

pm_dict = {
    "hello": "greetings",
    "friend": "m'hearty",
    "boy": "fine fellow",
    "sir": "boss",
}

pirate_dict = {
    "hello": "ahoy",
    "hi": "arrr",
    "my": "me",
    "friend": "m'hearty",
    "boy": "laddy",
    "girl": "lassie",
    "sir": "matey",
    "miss": "proud beauty",
    "stranger": "scurvy dog",
    "boss": "foul blaggart",
    "where": "whar",
    "is": "be",
    "the": "th'",
    "you": "ye",
    "old": "barnacle covered",
    "happy": "grog-filled",
    "nearby": "broadside",
    "bathroom": "head",
    "kitchen": "galley",
    "pub": "fleabag inn",
    "stop": "avast",
    "yes": "aye",
    "no": "nay",
    "yay": "yo-ho-ho",
    "money": "doubloons",
    "treasure": "booty",
    "strong": "heave-ho",
    "take": "pillage",
    "drink": "grog",
    "idiot": "scallywag",
    "sea": "briney deep",
    "vote": "mutiny",
    "song": "shanty",
    "drunk": "three sheets to the wind",
    "lol": "yo ho ho",
    "talk": "parley",
    "fail": "scupper",
    "quickly": "smartly",
    "captain": "cap'n",
}



_PIRATE_PHRASES = [
    "batten down the hatches!",
    "splice the mainbrace!",
    "thar she blows!",
    "arrr!",
    "weigh anchor and hoist the mizzen!",
    "savvy?",
    "dead men tell no tales.",
    "cleave him to the brisket!",
    "blimey!",
    "blow me down!",
    "avast ye!",
    "yo ho ho.",
    "shiver me timbers!",
    "blisterin' barnacles!",
    "ye flounderin' nincompoop.",
    "thundering typhoons!",
]



def load_translations(filename):
    """
    takes a file in the form of:
    original1:tranlated1
    original2:tranlated2
    original3:tranlated3
    ...
    originaln:tranlatedn

    and converts it into a tranlation dictionary
    
    """
    d = {}
    f = open(filename)
    for line in f.readlines():
        line = line.rstrip()
        (english,pirate) = line.split(",")
        d[english] = pirate
    return d


def translate(dict, text):
    """
    return a new string of text where every word
    in that is a key in the dictionary is replaced
    by the value from the dictionary
    """
    result = []
    for word in text.split():
        if word in dict.keys():
            result.append(dict[word])
        else:
            result.append(word)
    return " ".join(result)


def translate_lines(dict,text):
    result = ""
    for line in text.split("\n"):
        result = result + translate(dict,line) + "\n"

    return result


def translate_pirate(text):
    return translate_lines(pirate_dict,text)

def translate_pm(text):
    return translate_lines(pm_dict,text)


if __name__=='__main__':
    which_filter = ""
    if len(sys.argv) < 2:
        # print a message since they didn't specify
        print("Usage: " + sys.argv[0] + "-p|-m")
        #sys.exit(0) # and exit the program
    elif sys.argv[1] == '-p':
        which_filter = 'pirate'
    else:
        which_filter = 'pm'


    text = ""
    for line in sys.stdin:
        text = text + line

    if which_filter == "pirate":
        result = translate_pirate(text)
    else:
        result = translate_pm(text)
    print(result)
        
