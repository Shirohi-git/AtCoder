def main():
    dic = str.maketrans(ALP_s, ALP_s[::-1])
    obv = sorted(range(N), key=lambda x: S[x])
    rev = sorted(range(N), key=lambda x: S[x].translate(dic))

    res = [[0, 0] for _ in range(N)]
    for i in range(N):
        res[obv[i]][0] = i+1
        res[rev[i]][1] = i+1

    inv2 = pow(2, MOD9-2, MOD9)
    for ri in res:
        print(sum(ri) * inv2 % MOD9)
    return


if __name__ == '__main__':
    N = int(input())
    S = [input() for _ in range(N)]
    MOD9 = 998244353
    ALP_s = "abcdefghijklmnopqrstuvwxyz"

    main()
