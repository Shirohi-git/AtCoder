def nearlist(n0):
    res = [[] for _ in range(n0)]
    for i, (a, b) in enumerate(AB):
        res[a-1].append(i)
        res[b-1].append(i)
    return res


def bfs(n0, near0):
    flag = [(i+1 in AB[i]) for i in range(n0)]
    que = [i for i in range(n0) if flag[i]]

    for q in que:
        for i in near0[q]:
            if flag[i]:
                continue
            flag[i] = 1
            que.append(i)
    que = [qi+1 for qi in que]
    return que[::-1] if len(que) == N else [-1]


def main():
    near = nearlist(N)
    ans = bfs(N, near)
    return print(*ans, sep='\n')


if __name__ == '__main__':
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]

    main()
