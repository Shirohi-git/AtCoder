s = str(input()) + '0'
ans = [0] * (len(s))

cnt = 0
for i in range(len(s)):
    ans[i] = cnt
    if s[i] == '<':
        cnt += 1
    else:
        cnt = 0

cnt = 0
for i in range(len(s))[::-1]:
    ans[i] = max(cnt,ans[i])
    if s[i-1] == '>':
        cnt += 1
    else:
        cnt = 0

print(sum(ans))
