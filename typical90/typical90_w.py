def make_dict():
    stack = [0, 1]
    for i in range(W+2):
        bfo, now = 1 << i, 1 << (i+1)
        stack += [now + num for num in stack if (bfo & num) == 0]

    large = stack[-1]
    res = [-1] * (large + 1)
    for i in range(len(stack)):
        res[stack[i]] = i
    return len(stack), res, stack


def main():
    dp_size, dict, rvdict = make_dict()
    pow2w, judge = 1 << (W + 2), (1 << (W + 2)) + 7

    nowdp = [0] * dp_size
    nowdp[0] = 1
    for i in range(H+1):
        for j in range(W+2):
            nxtdp = [0] * dp_size
            for bit, cnt in zip(rvdict, nowdp):
                if cnt == 0:
                    continue
                nxt0 = dict[bit >> 1]
                nxtdp[nxt0] += cnt
                nxtdp[nxt0] -= MOD1 * (nxtdp[nxt0] > MOD1)
                if ((C[i][j] == '.') and ((bit & judge) == 0)):
                    nxt1 = dict[(bit >> 1) + pow2w]
                    nxtdp[nxt1] += cnt
                    nxtdp[nxt1] -= MOD1 * (nxtdp[nxt1] > MOD1)
                    continue
            nowdp = nxtdp[:]

    ans = sum(nowdp) % MOD1
    return print(ans)


MOD1 = int(1e9 + 7)
if __name__ == '__main__':
    H, W = map(int, input().split())
    C = ['#' * (W+2)] + ['#' + input() + '#' for _ in range(H)]

    main()
