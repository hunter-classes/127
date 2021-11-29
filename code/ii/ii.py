import csv

def clean(line):
    """
    takes in a string and returns a cleaned string.
    1. convert to lower case
    2. only keep letters and tab,space,newline
    """
    line = line.lower()
    letters_to_keep = 'abcdefghijklmnopqrstuvwxyz\t \n'
    # result = ""
    # for letter in line:
    #     if letter in letters_to_keep:
    #         result = result + letter
    result = [x for x in line if x in letters_to_keep]
    cleaned = "".join(result)
    return cleaned
    
def remove_stop_words(line):
    f = open("stopwords.txt")
    stopwords = f.read().split()
    result = [x for x in line.split() if x not in stopwords]
    line = " ".join(result)
    return line

def add_statement(index,key,statement):
    for word in statement.split():
        index.setdefault(word,[])
        if key not in index[word]:
            index[word].append(key)
    return index



f = open("last_statements_full.csv", encoding='Latin-1')

reader = csv.DictReader(f)

people = {}
index = {}

for item in reader:
    key = item['TDCJNumber']
    people[key] = item
    statement = clean(item['LastStatement'])

    # we might not want to remove the stop words
    statement = remove_stop_words(statement)
    index = add_statement(index,key,statement)

