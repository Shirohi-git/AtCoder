from collections import Counter

n = int(input())
s = [input() for _ in range(n)]

scnt = Counter(s)
cnt = max(scnt.values())
ans = sorted(k for k in scnt if scnt[k] == cnt)
print(*ans, sep='\n')
