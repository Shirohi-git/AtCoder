from itertools import combinations


def isOK(num):
    lst = [0] * 32
    for si in stt:
        idx = sum(2**j * (si[j] >= num) for j in range(5))
        lst[idx] |= 1
    for cmb in combinations(range(32), 3):
        tmp = 0
        for id in cmb:
            tmp |= id * lst[id]
        if tmp == 31:
            return True
    return False


def binary():
    l, r = -1, 10**10
    while abs(r - l) > 1:
        mid = (l + r) // 2
        if isOK(mid):
            l = mid
        else:
            r = mid
    return l


n = int(input())
stt = [list(map(int, input().split())) for _ in range(n)]
print(binary())
