h, w = map(int, input().split())
mod2 = lambda x: int(x) % 2
a = [list(map(mod2, input().split())) for _ in range(h)]

cnt, ans, rvs = 0, [], -1
for i, ai in enumerate(a):
    rvs *= -1
    for j in range(w)[::rvs]:
        if cnt == 1:
            ans.append([bi + 1, bj + 1, i + 1, j + 1])
            ai[j] += 1
        cnt = int(ai[j] == 1)
        bi, bj = i, j

print(len(ans))
for q in ans:
    print(*q)
