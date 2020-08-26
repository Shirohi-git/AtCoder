h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]
for i in range(h):
    a[i] = [aij % 2 for aij in a[i]]

cnt, ans = 0, []
for i, ai in enumerate(a):
    for j in range(w)[::(i % 2) * (-2) + 1]:
        if cnt == 1:
            ans.append([bi + 1, bj + 1, i + 1, j + 1])
            ai[j] += 1
        cnt = int(ai[j] == 1)
        bi, bj = i, j

print(len(ans))
for q in ans:
    print(*q)
