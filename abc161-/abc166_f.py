def move(X, Y, cnt, x, y):
    p = (y > x) - (x > y)
    if x == y == 0:
        return exit(print('No'))
    elif x == y and cnt < n:
        p += (X in s[cnt])
        p += (-p - 1) * (Y in s[cnt])
    ans.append(X if p == 1 else Y)
    return x + p, y - p

n, a, b, c = map(int, input().split())
s = [input() for i in range(n)]

ans = ['Yes']
for i in range(n):
    if s[i] == 'AB':
        a, b = move('A', 'B', i + 1, a, b)
    elif s[i] == 'AC':
        a, c = move('A', 'C', i + 1, a, c)
    elif s[i] == 'BC':
        b, c = move('B', 'C', i + 1, b, c)
print(*ans, sep='\n')
