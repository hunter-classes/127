def s_or(index,words):
    """
    return a list of all keys in the index
    that contain any of the words
    """
    result = []
    for word in words:
        result = result + index[word]
    return list(set(result))

def s_and(index,words):
    """
    return a list of the keys such that the key has ALL
    the words in it.
    """
    result = index[words[0]]
    for word in words[1:]:
        result = list(set(result) & set(index[word]))
    return result
        
