
# read in the entire file
# as a big string of characters
# f = open("data.dat")
# data = f.read() 

# each time we do f.readline()
# we read in the next line 
# line = f.readline()
# print(line)
# f.seek(0)
# line = f.readline()
# print(line)


f = open('data.dat')
data = f.read()

f.close()
f = open('data.dat')
lines = f.readlines()
