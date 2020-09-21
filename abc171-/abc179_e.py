n, x, m = map(int, input().split())

num, lst = set(), []
for i in range(n):
    num.add(x), lst.append(x)
    x = x ** 2 % m
    if x in num:
        cnt, idx = i + 1, lst.index(x)
        break

ans = sum(num)
if x in num:
    div, mod = divmod(n - cnt, len(lst) - idx)
    ans += sum(lst[idx:]) * div
    ans += sum(lst[idx:idx + mod])
print(ans)
