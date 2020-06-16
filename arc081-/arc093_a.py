n = int(input())
a = [0] + list(map(int, input().split())) + [0]

move = [abs(a[i - 1] - a[i]) for i in range(1, n + 2)]
msum = sum(move)
for i in range(1, n + 1):
    tmp = - move[i - 1] - move[i] + abs(a[i - 1] - a[i + 1])
    print(msum + tmp)
