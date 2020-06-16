import math
from itertools import combinations as com


k = int(input())
num = [i for i in range(1, k+1)]
cnt = sum(num)

for a,b in com(num, 2):
    cnt += 6 * math.gcd(a, b)

for a,b,c in com(num, 3):
    cnt += 6*math.gcd(c,math.gcd(a, b))

print(cnt)
