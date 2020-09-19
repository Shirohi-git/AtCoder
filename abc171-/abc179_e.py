n, x, m = map(int, input().split())

lst, num = set(), []
for i in range(1, n + 1):
    lst.add(x), num.append(x)
    x = x ** 2 % m
    if x in lst:
        cnt, idx = i, num.index(x)
        break

ans = sum(num)
if x in lst:
    div, mod = divmod(n - cnt, len(num) - idx)
    ans += sum(num[idx:]) * div
    ans += sum(num[idx:idx + mod])
print(ans)
