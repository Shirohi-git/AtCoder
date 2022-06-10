from itertools import product

d, g = map(int, input().split())
pc = [list(map(int, input().split())) for _ in range(d)]

ans = 1000
d_sum = [i * p + c // 100 for i, (p, c) in enumerate(pc, 1)]
for bit in product([0, 1], repeat=d):
    point = g // 100 - sum(b * ds for b, ds in zip(bit, d_sum))
    cnt = sum(b * p for b, (p, c) in zip(bit, pc))
    if point > 0:
        num = max(i * (1 - b) for i, b in enumerate(bit, 1))
        tmp = (point + num - 1) // num
        if tmp < pc[num - 1][0]:
            point -= tmp * num
            cnt += tmp
    if point <= 0:
        ans = min(ans, cnt)
print(ans)
