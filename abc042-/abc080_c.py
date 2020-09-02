from itertools import product

n = int(input())
f = [list(map(int, input().split())) for _ in range(n)]
p = [list(map(int, input().split())) for _ in range(n)]

ans = -(10 ** 10)
for bit in product([0, 1], repeat=10):
    if sum(bit) == 0:
        continue
    gain = 0
    for pi, fi in zip(p, f):
        tmp = sum(bitj & fij for bitj, fij in zip(bit, fi))
        gain += pi[tmp]
    ans = max(ans, gain)
print(ans)
