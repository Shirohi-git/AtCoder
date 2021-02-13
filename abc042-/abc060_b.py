from math import gcd

a, b, c = map(int, input().split())
print('YES' if c % gcd(a, b) == 0 else 'NO')
