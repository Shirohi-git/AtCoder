def __replace(s):
    return s.replace('o', '1').replace('x', '0')


def main():
    ans = 0
    flg = (1 << M) - 1
    for i in range(N):
        for j in range(i):
            ans += ((S[i] | S[j]) == flg)
    return print(ans)


if __name__ == '__main__':
    N, M = map(int, input().split())
    S = [int(__replace(input()), 2) for _ in range(N)]

    main()
