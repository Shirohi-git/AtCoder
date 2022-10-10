def main():
    def int_sqrt(num):
        res = int(num**0.5)-1
        while (res+1)**2 <= num:
            res += 1
        return res

    def calc_xy(a, b, k):
        if k == 0:
            return INF
        x = max(0, (b+k-1)//k - a)
        res = k*(x+a)+x - b
        return res

    for a, b in AB:
        ans = INF
        root_b = int_sqrt(b-1)
        for q in range(root_b+1):
            k = (b+q) // (q+1)
            ans = min(ans, calc_xy(a, b, q))
            ans = min(ans, calc_xy(a, b, k))
        print(ans)
    return


if __name__ == '__main__':
    T = int(input())
    AB = [list(map(int, input().split())) for _ in range(T)]
    INF = 10**18

    main()
