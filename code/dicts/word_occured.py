import random

data = [random.randrange(100) for x in range(100)]

nums = {}

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

for number in data:
    # if number isn't in nums then set it to 1
    # but if it is, this line will do nothing
    nums.setdefault(number,1)

    # when we get here, nums[number] WILL exist (becuase
    # of the above line or maybe an earlier iteration fo the loop
    # so we can just add 1 to the count
    nums[number] = nums[number] + 1
    
    


