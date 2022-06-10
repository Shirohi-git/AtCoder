from fractions import gcd

n, s = map(int, input().split())
x = list(map(int, input().split()))

ans = abs(s - x[0])
for i in x:
    ans = gcd(ans, abs(s - i))
print(ans)
