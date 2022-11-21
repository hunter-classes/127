import csv

# flawed example using split
# f = open("demo.csv")
# for line in f.readlines():
#     print(line)
#     line = line.strip()
#     print(line.split(","))

# Example using csv module into a list
# reader = csv.reader(open("demo.csv"))
# for line in reader:
#     print(line)

# Example - average the ages
# reader = csv.reader(open("demo.csv"))
# num_people = 0
# sum = 0
# for line in reader:
#     num_people = num_people + 1
#     sum = sum + int(line[2])
# print(sum/num_people)

# can use list comprehensions
# reader = csv.reader(open("demo.csv"))
# ages = [int(line[2]) for line in reader]

# using a csv.reader on a dataset
# where the first line are the field/column names
# reader = csv.reader(open("movies.csv"))
# full_data = [x for x in reader]
# field_names = full_data[0]
# data = full_data[1:]

# using the csv.DictReader
# reader = csv.DictReader(open("movies.csv"))
# for item in reader:
#     print(item)

# using csv.DictReader to create a list of dictionaries
# reader = csv.DictReader(open("movies.csv"))
# data = []
# for item in reader:
#     data.append(item)

# using DictReader and list comprehensions
reader = csv.DictReader(open("movies.csv"))
data = [x for x in reader]

# get all the comedy ratings using a loop
#comedy=[]
#for item in data:
#    comedy.append(int(item['Comedy']))

# get all comedy using a comprehension
comedy = [int(x['Comedy']) for x in data] 

# get all people who like comedy (>5)
likes_comedy = [ x for x in data if int(x['Comedy'])>7]

# also likes horror
likes_comedy_and_horror = [x['Code name'] for x in likes_comedy if int(x['Horror']) > 6]
