from bisect import bisect

n, t = map(int, input().split())
a = list(map(int, input().split()))

lst1, lst2 = [0], [0]
for ai in a[:n // 2]:
    lst1 += [li + ai for li in lst1]
for ai in a[n // 2:]:
    lst2 += [li + ai for li in lst2]
lst1 = sorted(lst1 + [-sum(a)])

ans = 0
for t2 in lst2:
    idx = bisect(lst1, t - t2) - 1
    ans = max(ans, t2 + lst1[idx])
print(ans)
