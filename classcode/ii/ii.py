import csv
def clean(text):
    """
    clean the text - turn all lower case, remove unwanted chars
    """
    letters_to_keep="abcdefghijklmnopqrstuvwxyz \t\n"
    text = text.lower()
    cleaned = [x for x in text if x in letters_to_keep]
    return "".join(cleaned)

 
def add_text_to_index(index, document, text):
    # go through the text a word a a time
    # and for each word add the  document to index entry
    # that has the word as the key
    for word in text.split():
        index.setdefault(word,[])
        if document not in index[word]:
            index[word].append(document)
    return index

def build_index_from_file(filename):
    reader = csv.DictReader(open(filename,encoding='Latin-1'))
    index = {}
    people = {}
    for line in reader:
        document = line['TDCJNumber']
        people[document] = line
        text = line['LastStatement']
        text = clean(text)
        index = add_text_to_index(index, document, text)
    return (people,index)


# example call: (p,i) = build_index_from_file("last_statements_full.csv")

