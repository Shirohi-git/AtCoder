s, t = input(), input()
l = set(list('atcoder@'))

for si, ti in zip(s, t):
    if si == '@' or ti == '@':
        if (si not in l) or (ti not in l):
            print('You will lose')
            break
    elif si != ti:
        print('You will lose')
        break
else:
    print('You can win')
