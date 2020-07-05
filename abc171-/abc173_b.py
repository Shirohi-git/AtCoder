from collections import Counter

n = int(input())
s = Counter([input() for _ in range(n)])

for j in ['AC', 'WA', 'TLE', 'RE']:
    print(j, 'x', s[j])
