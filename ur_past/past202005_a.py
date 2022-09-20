s = str(input())
t = str(input())

S, T = s.upper(), t.upper()
if s == t:
    print('same')
else:
    print('case-insensitive' if S == T else 'different')
