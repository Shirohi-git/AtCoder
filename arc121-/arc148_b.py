def main():
    if 'p' not in S:
        return print(S)

    stt = S.index('p')
    dic = str.maketrans("dp", "pd")
    ans = S[stt:stt+1][::-1].translate(dic) + S[stt+1:]
    for gol in range(stt+1, N+1):
        res = S[stt:gol][::-1].translate(dic) + S[gol:]
        ans = min(ans, res)
    return print(S[:stt] + ans)


if __name__ == '__main__':
    N = int(input())
    S = input()

    main()
