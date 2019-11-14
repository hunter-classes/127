import csv

# f = open("data.csv")

# for line in f.readlines():
#     data = line.split(",")
#     print(data)

f = open("data.csv",encoding="Latin-1")
reader = csv.reader(f)

for item in reader:
    print(item)

print()
print("--------------------------")
print()

f = open("data.csv",encoding="Latin-1")
reader = csv.DictReader(f)

people = {}
for item in reader:
    people[item['id']] = item

print(people)
