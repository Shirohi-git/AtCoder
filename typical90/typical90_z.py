def nearlist(n0):
    res = [set() for _ in range(n0)]
    for a, b in AB:
        res[a - 1].add(b - 1)
        res[b - 1].add(a - 1)
    return res


def bfs(s0, n0, near0):
    dist = [-1] * n0
    dist[s0] = 0
    que = [s0]

    for q in que:
        for i in near0[q]:
            if dist[i] > -1:
                continue
            dist[i] = dist[q] ^ 1
            que.append(i)
    return dist


def main():
    near = nearlist(N)
    dist = bfs(0, N, near)
    odd = [i+1 for i in range(N) if dist[i]][:N//2]
    evn = [i+1 for i in range(N) if 1-dist[i]][:N//2]
    return print(*(odd if (2*len(odd) >= N) else evn))


if __name__ == '__main__':
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N-1)]

    main()
