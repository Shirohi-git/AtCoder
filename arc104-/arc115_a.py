n, m = map(int, input().split())
s = [input() for _ in range(n)]

odd = sum(si.count('0') % 2 for si in s)
print(odd * (n - odd))
