import csv

def decode_csv_manually(filename):
    result = []
    f = open(filename)
    for text in f.readlines():
        text = text.rstrip()
        line = text.split(",")
        result.append(line)
    return result
        
        
def decode_csv_list(filename):
    result = []
    f = open(filename)
    for line in csv.reader(f):
        result.append(line)
    return result

def decode_csv_dict(filename):
    result = []
    f = open(filename)
    for line in csv.DictReader(f):
        result.append(line)
    return result
