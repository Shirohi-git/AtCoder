a, b, w = map(int, input().split())
w *= 1000

s, l = 10 ** 6, 0
for i in range(10 ** 6 + 1):
    if i * a <= w <= i * b:
        s, l = min(s, i), max(l, i)
print(*[s, l] if l > 0 else['UNSATISFIABLE'])
