n, k = map(int, input().split())
a = list(map(int, input().split()))
x = 0
for i in range(n):
    for j in range(i+1, n):
        if a[i] > a[j]:
            x += 1
y = 0
for i in range(n):
    for j in range(n):
        if a[i] > a[j]:
            y += 1
cnt = (x*k)+(k*(k-1)//2*y)
print(cnt % (10**9+7))