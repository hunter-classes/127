import csv
import searches as s

def clean(line):
    line = line.lower()
    letters_to_keep="abcdefghijklmnopqrstuvwxyz \t\n"
    cleaned = [x for x in line if x in letters_to_keep]
    return "".join(cleaned)

def add_statement(index,k,statement):
    for w in statement.split():
        index.setdefault(w,[])
        if k not in index[w]:
            index[w].append(k)
    return index

            


#f = open("last_statements_20.csv",encoding="Latin-1")
f = open("last_statements_full.csv",encoding="Latin-1")
reader = csv.DictReader(f)

def getcountstring(index,word):
    count = 0
    try:
        count = len(index[word])
    except:
        pass
    return  str(count) + " : "+word

people={}
index={}
for item in reader:
    k = item['TDCJNumber']
    people[k]=item
    statement = clean(item['LastStatement'])
    index = add_statement(index,k,statement)

#for w in index:
#    print(getcountstring(index,w))

b = s.and_search(index,['sorry','love'])
for id in b:
    print(people[id]['Age'])
print(len(b))
