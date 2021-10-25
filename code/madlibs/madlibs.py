import random

nouns = ['dog','cat','hammer','baseball']
verbs = ['ran','ate','hit','tickled']
names = ['horatio','penelope','antiope','dimitrious']
adjectives = ['hungry','scary','tired','sedintary']

def madlibify(story):
    result_list = []
    for word in story.split():
        lastchar = word[-1]
        if lastchar in ".!?":
            word = word.rstrip(lastchar)
            suffix=lastchar
        else:
            suffix=''
            
        if word == "<NOUN>":
            newword = random.choice(nouns)
        elif word == "<VERB>":
            newword = random.choice(verbs)
        elif word == "<NAME>":
            newword = random.choice(names)
        elif word == "<ADJECTIVE>":
            newword = random.choice(adjectives)
        else:
            newword = word

        newword = newword + suffix
        
        result_list.append(newword)
    return " ".join(result_list)

def main():
    story = open("story.text").read()
    result = madlibify(story)
    print(result)
if __name__=="__main__":
    main()
    
