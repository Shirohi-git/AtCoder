n, m = map(int, input().split())
py = [list(map(int, input().split())) for _ in range(m)]
pysort = sorted(py, key=lambda val: val[1])

pcnt, ans_d = [0] * (10 ** 5 + 1), {}
for i, j in pysort:
    pcnt[i] += 1
    ans_d[j] = str(pcnt[i])

for i, j in py:
    print(str(i).zfill(6) + ans_d[j].zfill(6))
