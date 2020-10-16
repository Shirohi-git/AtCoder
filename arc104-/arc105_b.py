from math import gcd

n = int(input())
a = list(map(int, input().split()))

ans = 0
for ai in a:
    ans = gcd(ans, ai)
print(ans)
