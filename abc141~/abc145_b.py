n = int(input())
s = str(input())
t = s[:n//2]
if t + t == s:
    print('Yes')
else:
    print('No')
