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

# alternatively, split on the newlines
lines = data.split("\n")
print(lines)


# or we can read a line at a time
f = open("sample.dat")
lines = f.readlines()
print(lines)

# we can use a list comprehension to get
# rid of the newlines
cleaned_lines = [line.strip() for line in lines]
print(cleaned_lines)
for line in cleaned_lines:
    print(line)
