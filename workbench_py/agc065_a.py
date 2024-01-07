# 全部互いに異なるならこれでいい、一番小さいところで切る
# 基本は降順、でも同じ数が連続しないように、最適な位置に

def main():
    if len(A) == len(set(A)):
        a = A * 2
        val, idx = K, 0
        for i, a1, a2 in zip(range(N), a, a[1:]):
            tmp = (a2 - a1) % K
            if val > tmp:
                val = tmp
                idx = i
    else:  # elif len(A) != len(set(A)):

        pass

    ans = 0
    for a1, a2 in zip(a[idx+1:idx+N], a[idx+2:]):
        ans += (a2 - a1) % K
    return print(ans)


if __name__ == '__main__':
    N, K = map(int, input().split())
    A = sorted(map(int, input().split()))[::-1]

    main()
