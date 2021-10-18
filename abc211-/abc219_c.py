def main():

    def change(word):
        res = []
        for wi in word:
            res.append(chr(X.index(wi) + ord('a')))
        return ''.join(res)

    s_dic = sorted((change(si), i) for si, i in S)
    for _, idx in s_dic:
        print(S[idx][0])
    return


if __name__ == '__main__':
    X = input()
    N = int(input())
    S = [(input(), i) for i in range(N)]

    main()
