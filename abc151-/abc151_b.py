n, k, m = map(int, input().split())
a = list(map(int, input().split()))

x = n * m - sum(a)
if x > k:
    print('-1')
else:
    print(max(0,x))