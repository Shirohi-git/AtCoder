def main():
    s_cnt = {si: 0 for si in S}
    for si in S:
        res = [si]
        if s_cnt[si] > 0:
            res.append('(' + str(s_cnt[si]) + ')')
        s_cnt[si] += 1
        print(''.join(res))
    return


if __name__ == '__main__':
    N = int(input())
    S = [input() for _ in range(N)]

    main()
