n = int(input())
csf = [list(map(int, input().split())) for _ in range(n - 1)]

for i, [ci, si, fi] in enumerate(csf):
    time = si + ci
    for cj, sj, fj in csf[i + 1:]:
        time = max(sj, time)
        time += (fj - (time % fj)) % fj + cj
    print(time)
print(0)
