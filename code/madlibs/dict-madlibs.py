import random

def build_substitution_dictionary(filename):
    d = {}
    f = open(filename)
    for line in f.readlines():
        line = line.strip()
        (part,word) = line.split(':')
        d.setdefault(part,[])
        d[part].append(word)
    return d    

def madlibify(story,substitutions):
    result_list = []
    for word in story.split():
        lastchar = word[-1]
        if lastchar in ".!?":
            word = word.rstrip(lastchar)
            suffix=lastchar
        else:
            suffix=''
            
        if word[0] == '<' and word[-1] == '>':
            # we have a substitution
            # so first pull out the key for the
            # substitution dictionary
            # that is, remove the < and >
            part = word[1:-1]

            # randomly select a substitution
            newword = random.choice(substitutions[part])
        else:
            newword = word
        newword = newword + suffix
        
        result_list.append(newword)
    return " ".join(result_list)

def main():
    story = open("story.text").read()
    substitutions = build_substitution_dictionary("substitutions.dat")
    result = madlibify(story,substitutions)
    print(result)

if __name__=="__main__":
    main()
    
