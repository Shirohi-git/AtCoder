t, n = map(int, input().split())

# 解説AC O(1)
exst = set(i+1 for i in range(100+t))
exst -= {(i+1) * (100+t) // 100 for i in range(100)}
lst = sorted(exst)

div, mod = divmod(n-1, len(lst))
ans = lst[mod] + (100+t) * div
print(ans)
