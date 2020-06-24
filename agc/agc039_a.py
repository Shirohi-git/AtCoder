s, k = input(), int(input())

if len(set(list(s))) == 1:
    print(len(s) * k // 2)
    exit()

ans, cnt = [], 1
for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        cnt += 1
    else:
        ans.append(cnt)
        cnt = 1
else:
    ans.append(cnt)

if s[0] != s[-1]:
    ans = [i//2 for i in ans]
    print(sum(ans) * k)
elif s[0] == s[-1]:
    f, m, l = ans[0] // 2, (ans[0] + ans[-1]) // 2, ans[-1] // 2
    ans = [i//2 for i in ans[1:-1]]
    print(f + sum(ans) * k + m * (k - 1) + l)
