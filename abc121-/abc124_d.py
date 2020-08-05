n, k = map(int, input().split())
s = input() + '#'

num = [0]
for i in range(1, n + 1):
    if s[i - 1] != s[i]:
        num.append(i)

ans, lennum = num[1], len(num)
for i in range((s[0] == '1') + 1, lennum, 2):
    r, l = max(i - 2, 0), min(i + 2 * k - 1, lennum - 1)
    ans = max(ans, num[l] - num[r])
print(ans)
