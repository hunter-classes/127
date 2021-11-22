import csv

# just using split (which doesn't work if you have , in the data)
# file = open("movies.csv")
# for line in file.readlines():
#     l = line.strip().split(",")
#     print(len(l))

# reader = csv.reader(open("movies.csv"))
# for line in reader:
#     print(line)

# processing a single column
# the if is to not count the first line wich are the labels
# reader = csv.reader(open("movies.csv"))
# sum = 0
# count = 0
# for line in reader:
#     print(line[6]) # only print out the 6th column (comedy)
#     if line[6] != 'Classic Q':
#         sum = sum + int(line[6])
#         count = count + 1
# print("The average comedy score is", sum/count)

# read all the data into a list of lists

# reader = csv.reader(open("movies.csv"))
# results = []
# for line in reader:
#     results.append(line)
# #print(results)
# print(results[4])
# print(results[4][1]+" gives "+results[0][6]+ " a rating of "+results[4][6])
# print(results[4][6])

# scan through once filtering out what we want
# reader = csv.reader(open("movies.csv"))
# for line in reader:
#     if line[6] != "Classic" and int(line[6]) >= 5:
#         print(line[1] + " likes classics" )

# read each line in the file into its own dictionary
# reader = csv.DictReader(open("movies.csv"))
# for item in reader:
#     print(item)

# reader = csv.DictReader(open("movies.csv"))
# results = [];
# for item in reader:
#     results.append(item)

# at this point results is a list where each item in the list is
# a dictionary

# classics_people = [  [ x['Code name'], x['Classic'] ]   for x in results if int(x['Classic']) > 7]
# print(classics_people)


# classics_scores = [ int(x['Classic']) for x in results]
# classics_avg = sum(classics_scores)/len(classics_scores)
# print(classics_scores)
# print(classics_avg)

reader = csv.DictReader(open("311.csv"))
for item in reader:
    print(item['Complaint Type'])
