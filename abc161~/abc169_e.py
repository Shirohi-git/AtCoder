from statistics import median

n = int(input())
ab = [list(map(int, input().split())) for _ in range(n)]

a = [ab[i][0] for i in range(n)]
b = [ab[i][1] for i in range(n)]
ma, mb = median(a), median(b)

if n % 2 == 0:
    print(int(2 * mb - 2 * ma + 1))
if n % 2 == 1:
    print(int(mb - ma + 1))
