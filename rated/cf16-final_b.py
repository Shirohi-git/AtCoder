n = int(input())

cnt = 0
for i in range(1, n + 1):
    cnt += i
    if cnt >= n:
        ans, exc = i, cnt - n
        break

for j in range(1, ans + 1):
    if exc != j:
        print(j)
