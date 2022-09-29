import piglatin
    
    

# Testing
test_word = "hello"
result = piglatin.piglatinify(test_word)
print(test_word," -> ",result)

test_word = "able"
result = piglatin.piglatinify(test_word)
print(test_word," -> ",result)

test_word = "Cable"
result = piglatin.piglatinify(test_word)
print(test_word," -> ",result)

test_word = "Able"
result = piglatin.piglatinify(test_word)
print(test_word," -> ",result)

test_word = "Able."
result = piglatin.piglatinify(test_word)
print(test_word," -> ",result)

test_word = "cable."
result = piglatin.piglatinify(test_word)
print(test_word," -> ",result)

test_word = "Table!"
result = piglatin.piglatinify(test_word)
print(test_word," -> ",result)

test_word = "deGromm"
result = piglatin.piglatinify(test_word)
print(test_word," -> ",result)

