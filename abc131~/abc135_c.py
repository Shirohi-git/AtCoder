n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
cnt = 0
for i in range(n):
    cnt += a[i]+a[i+1]-max(a[i]+a[i+1]-b[i], 0)
    a[i+1] = max(0, a[i+1]-max(0, b[i]-a[i]))
print(cnt)
