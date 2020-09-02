from itertools import product

n, m = map(int, input().split())
ks = [list(map(int, input().split())) for _ in range(m)]
p = list(map(int, input().split()))

ans = 0
for bit in product([0, 1], repeat=n):
    for ksi, pi in zip(ks, p):
        cnt = sum(bit[sij - 1] for sij in ksi[1:])
        if cnt % 2 != pi:
            break
    else:
        ans += 1
print(ans)
