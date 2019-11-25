
def or_search(index, words):
    """
    orsearch
    """
    result = []
    for word in words:
        result = result + index[word]
    return result
          
def and_search(index,words):
    result = index[words[0]]
    for w in words[1:]:
        result = list(set(result) & set(index[w]))
    return result
        
