import piglatin

source="How are you?"

def piglatinify_sentence(sentence):
    result_list = []
    for word in sentence.split():
        new_word = piglatin.piglatinify(word)
        result_list.append(new_word)
    result = ""
    #for item in result_list:
    #    result = result + item +" "
    #result = result.strip()
    result = " ".join(result_list)
    return result

        
        
result = piglatinify_sentence(source)
padded_result = ":"+result+":"
print(source)
print(padded_result)
