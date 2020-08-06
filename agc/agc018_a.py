from math import gcd

n, k = map(int, input().split())
a = list(map(int, input().split()))

num = 0
for ai in a:
    num = gcd(num, ai)
bool = (k % num) or (k > max(a))
print('IMPOSSIBLE' if bool else 'POSSIBLE')
