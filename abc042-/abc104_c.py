from itertools import product

d, g = map(int, input().split())
pc = [list(map(int, input().split())) for _ in range(d)]

d_sum = []
for i, (p, c) in enumerate(pc, 1):
    d_sum.append(i * 100 * p + c)

ans = 1000
for bit in product([0, 1], repeat=d):
    point = sum(b * ds for b, ds in zip(bit, d_sum))
    cnt = sum(b * p for b, (p, c) in zip(bit, pc))
    if point < g:
        num = max(i for i, b in enumerate(bit, 1) if b == 0)
        tmp = ((g - point) + (num * 100) - 1) // (num * 100)
        if tmp < pc[num - 1][0]:
            point += tmp * num * 100
            cnt += tmp
    if point >= g:
        ans = min(ans, cnt)
print(ans)
