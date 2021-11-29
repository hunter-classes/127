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
    

f = open("last_statements_20.csv", encoding='Latin-1')

reader = csv.DictReader(f)

people = {}
index = {}

for item in reader:
    key = item['TDCJNumber']
    people[key] = item
    statement = clean(item['LastStatement'])
    index = add_statement(index,key,statement)
    print()
