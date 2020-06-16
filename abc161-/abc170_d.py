n = int(input())
a = sorted(map(int, input().split()))

cnt = [0] * (a[-1] + 1)
for i in a:
    cnt[i] += 1
for i in set(a):
    if cnt[i] >= 1:
        for j in range(i * 2, a[-1] + 1, i):
            cnt[j] = 0
print(cnt.count(1))
