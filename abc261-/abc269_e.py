def main():
    def is_OK(num, stt):
        a, b, c, d = 1, N, 1, N
        if stt == 0:
            a = num
        elif stt == 1:
            c = num
        print('?', a, b, c, d)
        T = int(input())
        #T = ftest(a, b, c, d)
        return (N-num+1 != T)

    def binary(ok, ng, stt):
        while abs(ng - ok) > 1:
            mid = (ok + ng) // 2
            if is_OK(mid, stt):
                ok = mid
            else:
                ng = mid
        return ok

    def ftest(a, b, c, d):
        res = 0
        test = {(i, 1001-i) for i in range(1, 1000)}
        for x, y in test:
            if a <= x <= b and c <= y <= d:
                res += 1
        return res

    x = binary(0, N+1, 0)
    y = binary(0, N+1, 1)
    return print('!', x, y)


if __name__ == '__main__':
    N = int(input())

    main()
