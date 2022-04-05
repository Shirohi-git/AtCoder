def dfs(s0, n0, near0):
    dist, flag = [-1] * n0, [0] * n0
    dist[s0], flag[s0] = 0, 1
    stack = [s0]

    while stack:
        q = stack.pop()
        for i in near0[q]:
            if flag[i]:
                continue
            flag[i] = 1
            stack.append(i)
    return


def main():
    def v_idx(word):
        s1, s2, s3 = map(lambda x: ord(x) - Ord_A, word)
        return s1*58**2 + s2*58 + s3

    near = [[] for _ in range(58**3)]
    for si in S:
        near[v_idx(si[:3])].append(v_idx(si[-3:]))

    return


if __name__ == '__main__':
    N = int(input())
    S = [input() for _ in range(N)]
    Ord_A = ord('A')

    main()
