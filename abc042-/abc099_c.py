from itertools import product

n = int(input())

pow6 = [pow(6, i + 1) for i in range(6)]
pow9 = [pow(9, i) for i in range(6)][::-1]

ans = n
for l in product(range(6), repeat=6):
    cnt = sum(l)
    num = n - sum(pi * li for pi, li in zip(pow6, l))
    if num >= 0:
        for pi in pow9:
            cnt += num // pi
            num -= (num // pi) * pi
        ans = min(ans, cnt)
print(ans)
