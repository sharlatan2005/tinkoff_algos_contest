a, b, c, d = map(int, input().split())
l = -5000
r = 5000
x = (l + r) / 2
if (a < 0):
    a, b, c, d = -a, -b, -c, -d
while abs(r - l) > 10**(-10):
    x = (l + r) / 2
    if a*x*x*x + b*x*x + c*x + d > 0:
        r = x
    else:
        l = x
print(x)