from fractions import gcd
import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

cnt = 1
for i in range(n):
    cnt = a[i] * cnt // gcd(a[i], cnt)

b = [cnt // a[i] for i in range(n)]
print(sum(b) % (10**9+7))
