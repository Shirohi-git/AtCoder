def main():
    cnt = [1] + [0] * 7
    for si in S:
        if si in ATC:
            idx = ATC.index(si)
            cnt[idx+1] += cnt[idx]
            cnt[idx+1] %= MOD1
    return print(cnt[-1])


if __name__ == '__main__':
    N, S = int(input()), input()
    ATC = "atcoder"
    MOD1 = 10**9 + 7
    main()
