def main():
    dic = {'A': 'BC', 'B': 'CA', 'C': 'AB'}

    for t, k in TK:
        id, k = divmod(k-1, pow(2, min(t, MAX)))

        s = S[id]
        for i in range(t):
            if (k >> i) == 0:
                for _ in range((t-i) % 3):
                    s = dic[s][0]
                break
            s = dic[s][k >> i & 1]
        print(s)
    return


if __name__ == '__main__':
    S = input()
    Q = int(input())
    TK = [list(map(int, input().split())) for _ in range(Q)]
    MAX = 60

    main()
