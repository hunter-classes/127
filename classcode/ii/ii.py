import csv
def clean(text):
    """
    clean the text - turn all lower case, remove unwanted chars
    """
    return text


def add_text_to_index(index, document, text):
    # go through the text a word a a time
    # and for each word add the  document to index entry
    # that has the word as the key
    return index

def build_index_from_file(filename):
    reader = csv.DictReader(open(filename))
    index = {}
    for line in reader:
        document = line['document']
        text = line['text']
        text = clean(text)
        index = add_text_to_index(index,document,text)
    return index


