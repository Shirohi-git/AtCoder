def main():
    res = [0] * 26

    cnt = 1
    for si, sj in zip(S, S[1:]):
        if si == sj:
            cnt += 1
        else:
            idx = ord(si) - Ord_a
            res[idx] = max(cnt, res[idx])
            cnt = 1
    return print(sum(res))


if __name__ == '__main__':
    N = int(input())
    S = input() + '_'
    Ord_a = ord('a')

    main()
