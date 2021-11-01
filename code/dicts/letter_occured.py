import random

def find_max(l):
    m = l[0]
    for item in l:
        if item > m:
            m = item
    return m


data = """
this is a longer string with a lot of
words in it, we'll count the number of characters
and see how many times each appear 
and see that it's the same things as when we did this
for numbers the only difference is that this time
the keys to the dictionary are words
"""



letter_counts = {}

# here we're counting how many times each number appears
# in data but the first time we see a number it will give an error
# if we try to access it.
#to fixm we can use an if statement.
# if the number's already in the dict, add one to the current count
# otherwise set the initial count to 1

# for number in data:
#     if number in nums.keys():
#         nums[number]=nums[number]+1
#     else:
#         nums[number] = 1

# better way using the setdefault method

for letter in data:
    # if number isn't in nums then set it to 1
    # but if it is, this line will do nums.setdefault(number,1)

    # when we get here, nums[number] WILL exist (becuase
    # of the above line or maybe an earlier iteration fo the loop
    # so we can just add 1 to the count
    letter_counts.setdefault(letter,0)
    letter_counts[letter] = letter_counts[letter] + 1
    
v = letter_counts.values()
m = find_max(list(v))
largest_values = [x for x in letter_counts.keys() if letter_counts[x] == m]




