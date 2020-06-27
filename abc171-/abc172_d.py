n = int(input())

cnt = [1] * (n + 1)
for i in range(2, n + 1):
    for j in range(i, n + 1, i):
        cnt[j] += 1
print(sum(i * cnt[i] for i in range(1, n + 1)))
