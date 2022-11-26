def main():
    def func(x):
        return B*x + A/((x+1)**0.5)

    def ternary(ok, ng):
        def is_OK(m1, m2):
            return func(m1) >= func(m2)

        while abs(ng - ok) > 2:
            mid1 = (2 * ok + ng) // 3
            mid2 = (ok + 2 * ng) // 3

            if is_OK(mid1, mid2):
                ok = mid1
            else:
                ng = mid2
        return ok, ng

    p, q = ternary(0, 10**18)
    ans = 10**18
    for i in range(p, q+1):
        ans = min(ans, func(i))
    return print(ans)


if __name__ == '__main__':
    A, B = map(int, input().split())

    main()
