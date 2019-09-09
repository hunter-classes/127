

s1="Hello World"
print(s1[0])
print(s1[1])
print(len(s1))
s2 = s1[0:5] # slice from char 0 to char 5
print(s2)
s3  = s1[6:11]
print(s3)

print(s1[6:]) # slice from 6 to end
print(s1[:5]) # slice from 0 to 5
print(s1[-1]) # slice of the last char (wraparound)
