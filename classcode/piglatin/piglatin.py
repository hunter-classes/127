
def piglatinify(word):
    """
    word   : a single word
    return : the word converted into piglatin
    
    rules  : starts with a vowel --> append "ay"
             otherwise --> move first to last and append "ay"
    """
    
    if len(word) == 0:
        return word
    
    first = word[0]
    if first in "aeiou":
        result = word + "ay"
    else:
        result = word[1:] + first + "ay"
    return result

x = piglatinify("hello")
print("ellohay : ",x)
x = piglatinify("zero")
print("erozay : ",x)
x = piglatinify("")
print("nothing : ",x)
x = piglatinify("eyeball")
print("eyeballay : ",x)

