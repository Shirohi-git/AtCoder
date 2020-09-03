n = int(input())

num = n + (n % 2 == 0)
cnt, ans = 0, []
for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        if i + j != num:
            cnt += 1
            ans.append((i, j))

print(cnt)
for i, j in ans:
    print(i, j)
