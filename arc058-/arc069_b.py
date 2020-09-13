from itertools import product

n, s = int(input()), input()

for bfo2, bfo1 in product(['S', 'W'], repeat=2):
    ans = [bfo2, bfo1]
    for i in s:
        if ((bfo1 == 'S' and i == 'o')
                or (bfo1 == 'W' and i == 'x')):
            ans.append(bfo2)
        elif ((bfo1 == 'S' and i == 'x')
                or (bfo1 == 'W' and i == 'o')):
            ans.append(*({'S', 'W'} - {bfo2}))
        bfo1, bfo2 = ans[-1], bfo1
    if ans[:2] == ans[-2:]:
        print(*ans[1:-1], sep='')
        break
else:
    print(-1)
