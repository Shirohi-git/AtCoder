from itertools import product


def main():
    ans = 0
    for bit in product([0, 1], repeat=H):
        if sum(bit) == 0:
            continue
        idx = [i for i in range(H) if bit[i]]
        cnt = {pj: 0 for pj in P[idx[0]]}
        for j in range(W):
            num = P[idx[0]][j]
            if all(P[i][j] == num for i in idx):
                cnt[num] += 1
        ans = max(ans, max(cnt.values()) * sum(bit))
    return print(ans)


if __name__ == '__main__':
    H, W = map(int, input().split())
    P = [list(map(int, input().split())) for _ in range(H)]

    main()
