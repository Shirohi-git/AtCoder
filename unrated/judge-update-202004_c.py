from itertools import permutations as permu

a, b, c = map(int, input().split())

a1 = [0] * 3
a2 = [0] * 3
a3 = [0] * 3
a1[0] = 1
num = [i for i in range(2, a+b+c+1)]
ans = 0

for list in permu(num):
    for i in range(1, a):
        a1[i] = list[i-1]
    for j in range(b):
        a2[j] = list[j + a-1]
    for k in range(c):
        a3[k] = list[k + a + b-1]

    flag = 0
    for i in range(a-1):
        if a1[i+1] <= a1[i]:
            flag = 1
    for j in range(b-1):
        if a2[j+1] <= a2[j]:
            flag = 1
    for k in range(c-1):
        if a3[k+1] <= a3[k]:
            flag = 1

    for i in range(3):
        if (a1[i] * a2[i] != 0) and (a2[i] <= a1[i]):
            flag = 1
        if (a2[i] * a3[i] != 0) and (a3[i] <= a2[i]):
            flag = 1

    if flag == 0:
        ans += 1

print(ans)
