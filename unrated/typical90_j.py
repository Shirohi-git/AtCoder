n = int(input())
cp = [list(map(int, input().split())) for _ in range(n)]
q = int(input())
lr = [list(map(int, input().split())) for _ in range(q)]

acc1, acc2 = [0], [0]
for c, p in cp:
    acc1.append(acc1[-1]+p*(c == 1))
    acc2.append(acc2[-1]+p*(c == 2))
for l, r in lr:
    ans1 = acc1[r]-acc1[l-1]
    ans2 = acc2[r]-acc2[l-1]
    print(ans1, ans2)
