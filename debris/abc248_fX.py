def main():
    # なんとなくとりあえず最小全域木の数を求めてみた
    # 使わなかった辺の数を数えてDP, これが二乗の源泉っぽいな？
    # 実装するには残り時間が足りない。

    ans = [1, 1] + [0] * (N-2)
    for _ in range(2, N+1):
        nxt = [1] + [0] * (N-1)
        for i in range(1, N):
            nxt[i] = nxt
        b_ok, b_ng = cmb
        ok = (b_ok * 3 + b_ng) % P
        ng = (b_ok * 2 + b_ng) % P
        cmb = ok, ng

    return print(*ans)


if __name__ == '__main__':
    N, P = map(int, input().split())

    main()
