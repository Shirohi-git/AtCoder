from itertools import product

n, m = map(int, input().split())
ks = [list(map(int, input().split())) for _ in range(m)]
p = list(map(int, input().split()))

cnt = 0
for pat in product([0, 1], repeat=n):
    for ksi, pi in zip(ks, p):
        tmp = sum(pat[sij - 1] for sij in ksi[1:])
        if  tmp % 2 != pi:
            break
    else:
        cnt += 1
print(cnt)
