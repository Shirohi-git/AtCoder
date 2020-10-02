from itertools import product

n = int(input())
a = [input().split('.') + [''] for _ in range(n)]
a = [int(ai[0]) * pow(10, 9) + int(ai[1].ljust(9, '0')) for ai in a]

fact25 = [[0] * 19 for _ in range(19)]
for ai in a:
    f2, f5 = 0, 0
    for _ in range(18):
        j2, j5 = 1 - ai % 2, (5 - ai % 5) // 5
        f2, ai = f2 + j2, ai // (j2 * 1 + 1)
        f5, ai = f5 + j5, ai // (j5 * 4 + 1)
    fact25[f2][f5] += 1

ans = 0
lst = list(product(range(19), repeat=2))
for (p2, p5), (q2, q5) in product(lst, lst):
    if p2 + q2 >= 18 and p5 + q5 >= 18:
        TorF = ((p2, p5) == (q2, q5))
        ans += fact25[p2][p5] * (fact25[q2][q5] - TorF)
print(ans // 2)
