s = input()

a, b, c = s.count('a'), s.count('b'), s.count('c')
cnt = max(abs(a - b), abs(b - c), abs(c - a))
print('YES' if cnt <= 1 else 'NO')
