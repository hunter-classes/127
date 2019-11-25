
def countPlurals(line):
    count = 0
    for word in line.split():
        if word[-1]=='s':
            count = count + 1
    return count

def notPossesive(line):
    count = 0
    for word in line.split():

        if len(word) >= 3 and word[-1]=='s' and word[-2]!="'":
            count = count + 1
    return count



print("Question1 - countPlurasls")
print("-------------------------")
line = "this is a test of counting plurals"
print("countPlurals:",line,countPlurals(line))
line = ""
print("countPlurals:",line,countPlurals(line))
print("")
line = "this is a possesve's tests"
print("notPossesive:",line,notPossesive(line))
print("\n\n-----------------------------\n\n")

def makeAcronym(line):
    result = ""
    for word in line.lower().split():
        result = result + word[0]
    return result
print("Question2 - makeAcronym")
print("-------------------------")
line = "Laugh out Loud"
print("makeAcronym:",line,makeAcronym(line))
print("")
print("\n\n-----------------------------\n\n")
        


scores = {
    "aeioulnrst": 1,
    "dg": 2,
    "bcmp": 3,
    "fhvwy": 4,
    "k": 5,
    "jx": 8,
    "qz": 10
}


def score(word):
    score = 0
    for letter in word:
        for scoreletters in scores:
            if letter in scoreletters:
                score = score + scores[scoreletters]
    return score


print("Question3 - score")
print("-------------------------")
print("score('hello')",score('hello'))

