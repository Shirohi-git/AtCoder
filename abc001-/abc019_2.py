s = input()

cnt, ans = 1, [s[0]]
for i in range(1,len(s)):
    if s[i] == s[i - 1]:
        cnt += 1
    elif s[i] != s[i - 1]:
        ans.append(str(cnt))
        ans.append(s[i])
        cnt = 1
else:
    ans.append(str(cnt))
print(''.join(ans))
