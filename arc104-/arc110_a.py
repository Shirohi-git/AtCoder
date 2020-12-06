from math import gcd


def lcm(X, Y):
    return (X * Y) // gcd(X, Y)


n = int(input())

ans = 1
for i in range(1, n):
    ans = lcm(ans, i + 1)
print(ans + 1)
