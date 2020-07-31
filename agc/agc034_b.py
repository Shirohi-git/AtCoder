s = input().replace('BC', 'a')

ans, cnta = 0, 0
for i in range(len(s)):
    if s[i] == 'A':
        cnta += 1
    elif s[i] == 'a':
        ans += cnta
    else:
        cnta = 0
print(ans)
