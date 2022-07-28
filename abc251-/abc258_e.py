from itertools import accumulate


class Potato:
    def __init__(self, n, w, x):
        self.x = x
        self.nxt = [-1] * n
        self.cnt = [-1] * n
        self.sum = sum(w)
        self.acc = list(accumulate([0] + W*2))
    
    def calc_cntnxt(s):
        if self.cnt[s] >= 0:
            return
        return


def rho_alg(nxt):
    flag = [-1] * N
    rho = []
    now, cnt = 0, 0
    while flag[now] < 0:
        rho.append(now)
        flag[now] = cnt
        now, cnt = nxt[now], cnt+1
    stt_idx = rho.index(now)
    return rho, stt_idx


def main():
    ptt = Potato(N, W, X)
    rho, stt_id = rho_algo(ptt.nxt)
    ccl, ccl_len = rho[s_idx:], len(rho[s_idx:])
    ans = []
    for ki in K:
        ki -= 1
        if ki < stt_id:
            ans.append(ptt.cnt[rho[ki]])
        else:
            ki = (ki - stt_id) % ccl_len
            ans.append(ptt.cnt[ccl[ki]])
    return print(ans, sep='\n')


if __name__ == '__main__':
    N, Q, X = map(int, input().split())
    W = list(map(int, input().split()))
    K = [int(input()) for _ in range(Q)]

    main()