s = ''.join(sorted(input()))
t = ''.join(sorted(input(), reverse=True))

list = sorted([s, t])
print('Yes' if (s == list[0] and s != t) else 'No')
