import sys
input = sys.stdin.readline


k, n = map(int, input().split())
a = list(map(int, input().split()))

long = k-a[n-1]+a[0]
for i in range(1,n):
    long=max(long,abs(a[i]-a[i-1]))
print(k - long)
