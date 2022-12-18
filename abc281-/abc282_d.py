from collections import Counter

def main():
    def nearlist(n0, lst):
        res = [[] for _ in range(n0)]
        for a, b in lst:
            res[a - 1].append(b - 1)
            res[b - 1].append(a - 1)
        return res

    def is_bipartite(s, ini):
        stack = [(s, ini)]
        color[s] = ini
        while stack:
            q, c = stack.pop()
            for i in near[q]:
                if color[i] == c:
                    return False
                if color[i] == 0:
                    color[i] = -c
                    stack.append((i, -c))
        return True

    near = nearlist(N, UV)
    color = [0 for _ in range(N)]
    idx = 0
    for i in range(N):
        if color[i] == 0:
            idx += 1
            if not is_bipartite(i, idx):
                return print(0)

    cnt = Counter(color)
    ans = 0
    for i, ci in enumerate(color):
        ans += N - len(near[i]) - cnt[ci]
    return print(ans // 2)


if __name__ == '__main__':
    N, M = map(int, input().split())
    UV = [list(map(int, input().split())) for _ in range(M)]

    main()
