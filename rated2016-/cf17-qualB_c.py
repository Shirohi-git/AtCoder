def is_bipartite(s0,  n0, near0):
    color = [0 for i in range(n0)]
    stack = [(s0, 1)]
    while stack:
        q, c = stack.pop()
        for i in near0[q]:
            if color[i] == c:
                return []
            if color[i] == 0:
                color[i] = -c
                stack.append((i, -c))
    return [ci for ci in color if ci > 0]


def main():
    def nearlist(n0, lst0):
        res = [[] for _ in range(n0)]
        for a, b in lst0:
            res[a - 1].append(b - 1)
            res[b - 1].append(a - 1)
        return res

    near = nearlist(N, AB)
    ans = N * (N-1) // 2
    evn = is_bipartite(0, N, near)
    if evn:
        ans = (N-len(evn)) * len(evn)
    return print(ans - M)

if __name__ == '__main__':
    N, M = map(int, input().split())
    AB = [map(int, input().split()) for _ in range(M)]

    main()
    