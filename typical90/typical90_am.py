def dfs(s):
    cnt = [0] * (N-1)
    flag = [0] * N
    flag[s] = 1
    stack = [(s, -1)]

    while stack:
        q, edge = stack[-1]
        for idx in ITER[q]:
            i, j = AB[idx]
            i = (i-1 if (q != i-1) else j-1)
            if flag[i]:
                continue
            flag[i] = 1
            stack.append((i, idx))
            break
        else:
            stack.pop()
            if edge > -1:
                cnt[edge] += sum(cnt[idx] for idx in NEAR[q]) + 1
    return cnt


def main():
    for i, (a, b) in enumerate(AB):
        NEAR[a-1].append(i)
        NEAR[b-1].append(i)
    for i in range(N):
        ITER[i] = iter(NEAR[i])

    cnt = dfs(0)
    ans = sum((N-ci) * ci for ci in cnt)
    return print(ans)


if __name__ == "__main__":
    N = int(input())
    AB = [tuple(map(int, input().split())) for _ in range(N-1)]
    NEAR = [[] for _ in range(N)]
    ITER = [None] * N

    main()
