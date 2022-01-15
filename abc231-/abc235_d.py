def main():

    def ope(n, c):
        if n % A == 0 and ans[n//A] < 0:
            lst.append((n//A, c+1))
            ans[n//A] = c+1

        ns = str(n)
        if len(ns) == 1 or ns[1] == '0':
            return
        res = int(ns[1:] + ns[0])
        if ans[res] < 0:
            lst.append((res, c+1))
            ans[res] = c+1
        return

    ans = [-1] * INF
    ans[N] = 0
    lst = [(N, 0)]
    for num, cnt in lst:
        ope(num, cnt)
    return print(ans[1])


if __name__ == '__main__':
    A, N = map(int, input().split())
    INF = 10**7

    main()
