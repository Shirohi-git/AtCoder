from itertools import accumulate
n, k = map(int, input().split())
a = [0] + list(accumulate(map(int, input().split())))

btfl = []
for i in range(0, n):
    for j in range(i + 1, n + 1):
        btfl.append(a[j] - a[i])

# 解説AC
ans = 0
for i in range(50)[::-1]:
    num, cnt = ans + pow(2, i), 0
    for b in btfl:
        if num == num & b:
            cnt += 1
    if cnt >= k:
        ans = num
print(ans)
