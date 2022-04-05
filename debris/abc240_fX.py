def main(n, m, xy):
    def calc_ai(id):
        res, now = 0, 1
        for x, y in xy:
            if now > id:
                break
            nxt = max(id, now+y)
            res += (nxt+now) * (nxt-now) * x // 2
            now = nxt + 1
        print('calc', res)
        return res

    ans, idx, bfo = 0, 0, 0
    for x, y in xy:
        if x < 0 and bfo >= 0:
            cnt = (bfo-1) // x
            print('hoge',bfo, idx, cnt)

            if cnt <= y:
                ans = max(calc_ai(idx + cnt), ans)
        bfo += x*y
        idx += y
        print(bfo, idx)
    return ans


if __name__ == '__main__':
    T = int(input())

    ANS = []
    for _ in range(T):
        N, M = map(int, input().split())
        XY = [list(map(int, input().split())) for _ in range(N)]
        ANS.append(main(N, M, XY))
    print(*ANS, sep='\n')
