n, l = map(int, input().split())
s = [input() for _ in range(n)]
print(*sorted(s), sep='')
