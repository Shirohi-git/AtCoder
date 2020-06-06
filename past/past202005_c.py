from math import log

a, r, n = map(int, input().split())

if r > 1:
    lim = log(10 ** 9 / a, r)
    print('large' if n - 1 > lim else a * pow(r, n - 1))
else:
    print(a)
