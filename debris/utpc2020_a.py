def cal(x):
    t = x
    bfo = 0
    for x, a in xa:
        x = min(t, x + (a - bfo))
        if x < 0:
            return False
        bfo = a
    

def binary(l, r):
    while abs(r - l) > 1:
        num = (l + r) // 2
        if True:
            r = num
        else:
            l = num
    return r

n, l = map(int, input().split())
xa = [list(map(int, input().split())) for _ in range(n)]

