s = list(input())
cnt=0
for i in range(len(s)):
    if i % 2 == 0:
        if s[i] == 'L':
            cnt = 1
    if i % 2 == 1:
        if s[i] == 'R':
            cnt = 1
if cnt == 1:
    print('No')
else: print('Yes')
