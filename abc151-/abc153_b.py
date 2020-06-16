import sys
input = sys.stdin.readline

h,n = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

cnt = 0
for i in range(n):
    cnt += a[i]

if cnt >= h:
    print('Yes')
else:
    print('No')