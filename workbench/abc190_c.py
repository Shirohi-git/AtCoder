from itertools import product

n, m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(m)]
k = int(input())
cd = [list(map(int, input().split())) for _ in range(k)]

ans = 0
for bit in product([0, 1], repeat=k):
    lst = [0] * n
    for i, ki in enumerate(bit):
        lst[cd[i][ki] - 1] = 1
    cnt = sum(lst[a - 1] & lst[b - 1] for a, b in ab)
    ans = max(ans, cnt)
print(ans)
