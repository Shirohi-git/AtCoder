a = [list(map(int, input().split())) for _ in range(3)]
n = int(input())
b = set([int(input()) for i in range(n)])
ans = [[-1]*3 for _ in range(3)]

for i in range(3):
    for j in range(3):
        if a[i][j] in b:
            ans[i][j] = 0

cnt = 0
for i in range(3):
    if sum(ans[i]) == 0:
        cnt = 1
        break
    elif ans[0][i] + ans[1][i] + ans[2][i] == 0:
        cnt = 1
        break
    elif ans[0][0] + ans[1][1] + ans[2][2] == 0:
        cnt = 1
        break
    elif ans[0][2] + ans[1][1] + ans[2][0] == 0:
        cnt = 1
        break

if cnt == 1:
    print('Yes')
else:
    print('No')
