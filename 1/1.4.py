import math

c = float(input())

def f(x, c):
    return x**2 + math.sqrt(x + 1) - c

l, r, = 0, math.sqrt(c)
x = r

while (abs(f(x, c)) > 1e-6):
    x = (l + r) / 2
    if (f(x, c) > 0):
        r = x
    elif (f(x, c) < 0):
        l = x
    else:
        print(x)

print(x)