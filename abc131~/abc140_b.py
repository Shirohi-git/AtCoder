n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
cnt = 0
for i in range(n):
    cnt += b[a[i] - 1]
    if (a[i]-1 == a[i-1])&(i!=0):
        cnt += c[a[i - 1]-1]
print(cnt)