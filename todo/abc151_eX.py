import itertools as it

n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

ans=0
for i in it.combinations([i for i in range(n)], k):
    max_x = a[max(i)]
    min_x = a[min(i)]
    ans += (max_x - min_x)

print(ans%(10**9 +7))
