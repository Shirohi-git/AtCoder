def marge(lst, num):
    res, add = [], [li + num for li in lst]
    while lst and add:
        if lst[-1] <= add[-1]:
            res.append(lst.pop())
        elif lst[-1] > add[-1]:
            res.append(add.pop())
    return lst + add + res[::-1]


n, t = map(int, input().split())
a = list(map(int, input().split()))

lst1, lst2 = [0], [0]
for ai in a[:n // 2]:
    lst1 = marge(lst1, ai)
for ai in a[n // 2:]:
    lst2 = marge(lst2, ai)
lst1 += [-sum(a)]

ans, idx = 0, 0
for t2 in lst2[::-1]:
    while t2 + lst1[idx] > t:
        idx += 1
    ans = max(ans, t2 + lst1[idx])
print(ans)
