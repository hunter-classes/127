
def encode(input):
    index = 0
    count = 1
    encoded = []
    while index < len(input):
        next = index + 1
        while next < len(input) and  input[next] == input[index]:
            count = count + 1
            next = next + 1
        encoded.append([input[index],count])
        count = 1
        index = next
    return encoded

def decode(input):
    result = ""
    for item in input:
        result = result + item[0]*item[1]

    return result

def secs_to_hms(seconds):
    s = seconds % 60
    m = (seconds // 60) % 60
    h = seconds // 60 // 60
    return {'hours':h,'minutes':m,'seconds':s}
    
def hms_to_secs(hms):
    hourpart = hms['hours']*60*60 
    minpart = hms['minutes'] * 60
    secpart = hms['seconds']
    return hourpart + minpart + secpart

def addtimes(hms1,hms2):
    res = hms_to_secs(hms1) + hms_to_secs(hms2)
    return secs_to_hms(res)


# this isn't 100% correct but I accepted things similar to this.
# this doesn't account for multiples of the same letters
# to accomodate that you should remove words from letters as you use them
def scrabble(letters,word):
    for w in word:
        if w not in letters:
            return False
    return True

def scrabble_more_correct(letters,word):
    for w in word:
        if w not in letters:
            return False
        else:
            letters.replace(w,"",1) # the 1 means replace only 1
    return True


