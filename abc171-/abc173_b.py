from collections import Counter 

n = int(input())
s = Counter([input() for _ in range(n)])

print('AC x', s['AC'])
print('WA x', s['WA'])
print('TLE x', s['TLE'])
print('RE x', s['RE'])
