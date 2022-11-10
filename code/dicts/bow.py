
def clean(s):
    letters = []
    for l in s:
        if l.isalpha() or l==' ' or l=='\n':
            letters.append(l)
    result = "".join(letters)
    result = result.lower()
    return result 

def build_bow(data):
    counts = {}
    for word in data.split():
        counts.setdefault(word,0)
        counts[word] = counts[word]+1
        
    return counts



file = open("scandal.txt")


raw_data = file.read()
data = clean(raw_data)
bag = build_bow(data)
