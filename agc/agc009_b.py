def rec_dfs(s0, n0, edge0):

    def nearlist(n0, lst0):
        res = [[] for _ in range(n0)]
        for a, b in lst0:
            res[a - 1].append(b - 1)
            res[b - 1].append(a - 1)
        return res

    near0 = nearlist(N, edge0)
    near_it = [iter(ni) for ni in near0]

    cnt = [-1] * n0
    stack = ['s', s0]

    while len(stack) > 1:
        q = stack[-1]
        for i in near_it[q]:
            if i == stack[-2]:
                continue
            stack.append(i)
            break
        else:
            child = sorted(cnt[ni] for ni in near0[q])[::-1]
            cnt[q] = max(i+ci for i, ci in enumerate(child)) + 1
            stack.pop()
    return cnt[0]


def main():
    edge = [(i, ai) for i, ai in enumerate(A, 2)]
    ans = rec_dfs(0, N, edge)
    return print(ans)


if __name__ == '__main__':
    N = int(input())
    A = [int(input()) for _ in range(N-1)]

    main()
