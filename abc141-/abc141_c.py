n, k, q = map(int, input().split())
a = [int(input()) for i in range(q)]
b = [k-q] * n
for i in a:
    b[i - 1] += 1
for i in b:
    if i <= 0:
        print('No')
    else:
        print('Yes')
