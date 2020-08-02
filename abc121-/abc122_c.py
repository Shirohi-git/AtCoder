n, q = map(int, input().split())
s = input().replace('AC','#.')
lr = [list(map(int, input().split())) for _ in range(q)]

accs = [0]
for i in s:
    accs.append(accs[-1] + (i == '.'))
for l, r in lr:
    print(accs[r] - accs[l])
