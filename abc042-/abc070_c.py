from math import gcd

def lcm(X, Y):
    return (X * Y) // gcd(X, Y)

n = int(input())
t = [int(input()) for _ in range(n)]

ans = 1
for i in t:
    ans = lcm(ans, i)
print(ans)
