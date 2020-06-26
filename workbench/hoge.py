import sys
sys.setrecursionlimit(10 ** 7)


def tribonacci(n, TRI):
    if TRI[n - 1] > 0:
        return TRI[n - 1]
    elif n <= 2:
        TRI[n - 1] = 0
        return TRI[n - 1]
    elif n == 3:
        TRI[n - 1] = 1
        return TRI[n - 1]
    else:
        TRI[n - 1] = tribonacci(n - 1, TRI) + \
            tribonacci(n - 2, TRI) + tribonacci(n - 3, TRI)
        TRI[n - 1] %= 10007
        return TRI[n - 1]


n = int(input())

tri = [0] * n
tribonacci(n, tri)
print(tri[-1])
