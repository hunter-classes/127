
def f(a):
    a = a + 10
    return a

num = 20
print(num)
print(f(num))
print(num)
x = f(num)
num = f(num)
print(x,num)

z = 10
print(z)
z = z + 5
print(z)


a = 30
print(a)
x = f(a)
print(a,x)

