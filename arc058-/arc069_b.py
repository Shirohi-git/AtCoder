from itertools import product

n, s = int(input()), input()

ans = [-1]
for bfo2, bfo1 in product(['S', 'W'], repeat=2):
    lst = [bfo2, bfo1]
    for si in s:
        tmp = bfo1 + si
        if tmp in ['So', 'Wx']:
            lst.append(bfo2)
        if tmp in ['Sx', 'Wo']:
            lst.append('SW'.replace(bfo2, ''))
        bfo1, bfo2 = lst[-1], bfo1
    if lst[:2] == lst[-2:]:
        ans = lst[1:-1]
print(*ans, sep='')
