k = int(input())
s = list(map(int, list(input()[:-1])))
t = list(map(int, list(input()[:-1])))

scnt = [s.count(i) for i in range(10)]
tcnt = [t.count(i) for i in range(10)]
cnt = [si + ti for si, ti in zip(scnt, tcnt)]
allcom = (9 * k - 8) * (9 * k - 9)

pred_s = []
for j in range(1, 10):
    tmp = sum(i * 10 ** (scnt[i] + (i == j)) for i in range(1, 10))
    pred_s.append(tmp)
pred_t = []
for j in range(1, 10):
    tmp = sum(i * 10 ** (tcnt[i] + (i == j)) for i in range(1, 10))
    pred_t.append(tmp)

res = 0
for i, si in enumerate(pred_s, 1):
    for j, tj in enumerate(pred_t, 1):
        if cnt[i] + 1 + (i == j) > k or cnt[j] + 1 > k:
            continue
        if si > tj:
            res += (i == j) * (k - cnt[i]) * (k - cnt[j] - 1)
            res += (i != j) * (k - cnt[i]) * (k - cnt[j])
print(res / allcom)
