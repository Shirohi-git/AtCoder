n = int(input())
a = list(map(int, input().split()))

cnt, t = 0, 0
for i in range(1,n):
    if a[i] == a[i - 1] and t == 0:
        t = 0
    elif a[i] >= a[i - 1] and t >= 0:
        t = 1
    elif a[i] <= a[i - 1] and t <= 0:
        t = -1
    else:
        cnt += 1
        t = 0
else:
    cnt += 1
print(cnt)
