from itertools import accumulate

n = int(input())
a = sorted(list(map(int, input().split())))
asum = list(accumulate(a))

cnt= 1
for i in range(1,n):
    if asum[i - 1] * 2 >= a[i]:
        cnt += 1
    else:
        cnt = 1
print(cnt)
