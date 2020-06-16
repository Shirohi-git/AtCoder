s = str(input())
ans=''
for i in s:
    if i == '1' or '0':
        ans = ans + i
    if i == 'B' and len(ans) > 0:
        ans = ans[:-2]
print(ans)
