n = int(input())
h = list(map(int, input().split()))

cnt = [float('inf')]*n
cnt[0], cnt[1] = 0, abs(h[0]-h[1])
for i in range(2,n):
    cnt[i]=min(abs(h[i-1]-h[i])+cnt[i-1],abs(h[i-2]-h[i])+cnt[i-2])

print(cnt[n-1])
