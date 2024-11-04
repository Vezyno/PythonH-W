import math

x = 5
y = 2
z = 3
print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x//y)
print(x%y)
print(-x)
print(abs(-x))
print(x**2)
print(divmod(x, y))
print(pow(x, y, z))
print(round(math.pi, 3))
a = 5
b = 3
c = round(a/b, 3)
print(c)
x, t = 10, 1
# z = (9*math.pi*t + 10*math.cos(x)) * (math.exp(x)) / (math.sqrt(t) - abs(math.sin(t)))
# z = (9*math.pi*t + 10*math.cos(x)) * (math.exp(x)) / ((t**(1/2)) - abs(math.sin(t)))
print(round(z, 2))