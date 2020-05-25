import re
n = int(input())
s = [input() for i in range(n)]
pattern = '\w*(okyo)\w*(ech)\w*'
for i in range(n):
    if re.match(pattern, s[i]):
        print('Yes')
    else:
        print('No')
