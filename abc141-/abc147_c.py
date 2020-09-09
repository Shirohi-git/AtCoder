from itertools import product

n = int(input())
xy = []
for _ in range(n):
    a = int(input())
    tmp = [list(map(int, input().split())) for _ in range(a)]
    xy.append(tmp)

ans = 0
for bit in product([0, 1], repeat=n):
    for i, liar in enumerate(bit):
        if liar and any(bit[x - 1] != y for x, y in xy[i]):
            break
    else:
        ans = max(ans, sum(bit))
print(ans)
