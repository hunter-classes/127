import random
# make a list of foods
foods = ['pizza','burger','chocolate','wings','tuna','cheese']

# make list of random foods selected from the list
sample = []
sample_size = 200
for i in range(sample_size):
    f = random.choice(foods)
    sample.append(f)

    
# count how many of each food - slower version
# food_counts = {}
# for food in foods:
#     count = 0
#     for s in sample:
#         if s == food:
#             count = count + 1
#     food_counts[food]=count

# print(food_counts)

# count the number of each food - preferred way
food_counts = {}
for s in sample:
    food_counts.setdefault(s,0)
    food_counts[s] = food_counts[s] + 1
        
for k in food_counts:
    print(k+" : "+str(food_counts[k]))


print("\n")

for k,v in food_counts.items():
    print(k + " "*(10-len(k)) + " : " + '*'*v)

# print out the food counts in sorted order.
