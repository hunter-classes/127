# file input demo with some string stuff

s1='hello'
s2="Hello\nthis\nis\nmultiline but on one line"
s3="""
This is a multiline string
using triple quotes
"""

# strip strips off leading and trailing whitespace
# there's also rstrip() and lstrip()
# you can also give a parameter to say what to strip
stripped=s3.strip()

# read the whole file into a variable
f = open("sample.dat")
data = f.read()
print(data)
# split on whitespace so you get a list of words
words = data.split()
print(words)
print("\n--------\n")


# alternatively, split on the newlines
lines = data.split("\n")
print(lines)
print("\n--------\n")



# or we can read a line at a time
f = open("sample.dat")
lines = f.readlines()
print(lines)
print("\n--------\n")


# we can use a list comprehension to get
# rid of the newlines
cleaned_lines = [line.strip() for line in lines]
print(cleaned_lines)
for line in cleaned_lines:
    print(line)

# doing it in a for loop 
for line in open("sample.dat").readlines():
    cleaned_line = line.strip()
    print(cleaned_line)

print("\n--------\n")

# reading a line at a time

f = open("sample.dat")
l  = f.readline()
print(l)
l  = f.readline()
print(l)


# dealing with CSV the basic way
# a more advanced way would be to use the
# csv module
lines = open("sample.csv").readlines()
cleaned_lines = [line.strip() for line in lines]
print(cleaned_lines)
for line in cleaned_lines:
    line_list = line.split(",")
    print(line_list)
    print("name:",line_list[0])
    print("age:",line_list[1])
    print("eye color:",line_list[2])
    

print("\n--------\n")
# a more advanced way
lines = open("sample.csv").readlines()
cleaned_lines = [line.strip() for line in lines]
print(cleaned_lines)
for line in cleaned_lines:
    (name,age,eye_color) = line.split(",")
    print(name+" has " + eye_color + " eyes")
    
print("\n--------\n")

# we use split to split a string into a lits
# we use join to go the other way

list=["one","two","three","four","five"]

result_string1 = " ".join(list)
print(result_string1)

result_string2 = ",".join(list)
print(result_string2)

result_string3 = "-:-".join(list)
print(result_string3)

