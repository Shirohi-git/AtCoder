def main():
    def calculate(a, b, c, d):
        stt, x, y = (a-1)*M + c, (b-a+2)//2, (d-c+2)//2
        stt = y * (stt + (y-1))
        return x * (stt + M*(x-1)*y) % MOD9

    ans = []
    for a, b, c, d in ABCD:
        res = 0
        if (a+c) % 2 == 0:
            res += calculate(a, b, c, d)
            res += calculate(a+1, b, c+1, d)
        else:  # elif (a+c) % 2 == 1:
            res += calculate(a+1, b, c, d)
            res += calculate(a, b, c+1, d)
        ans.append(res % MOD9)
    return print(*ans, sep='\n')


if __name__ == '__main__':
    N, M = map(int, input().split())
    Q = int(input())
    ABCD = [list(map(int, input().split())) for _ in range(Q)]
    MOD9 = 998244353

    main()
