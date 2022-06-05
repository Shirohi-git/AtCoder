def ftoi(str):
    num1, num2 = (str+'.0').split('.')[:2]
    return int(num1)*ELE + int((num2+"0000")[:4])


def ceil(num, div):
    return (num + div - 1) // div


def binary(ok, ng, x):
    def is_OK(y):
        return (x-X)**2 + (y-Y)**2 <= R**2

    while abs(ng - ok) > 1:
        mid = (ok + ng) // 2
        if is_OK(mid):
            ok = mid
        else:
            ng = mid
    return ok


def main():
    ans = 0
    for xi in range(ceil(X-R, ELE), (X+R)//ELE+1):
        xi *= ELE
        ymx = binary(Y, INF, xi) // ELE
        ymn = ceil(binary(Y, -INF, xi), ELE)
        ans += max(ymx - ymn + 1, 0)
    return print(ans)


if __name__ == '__main__':
    ELE, INF = 10000, 10**10
    X, Y, R = map(ftoi, input().split())

    main()