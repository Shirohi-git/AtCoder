def main():
    flag = [1] * M
    near = [[] for _ in range(N)]
    for idx in range(M):
        for p in R[idx]:
            near[p-1].append(idx)

    ans = [-1] * N
    ans[0] = 0
    que = [0]
    for q in que:
        lst = []
        for idx in near[q]:
            if flag[idx]:
                lst += R[idx]
                flag[idx] = 0

        for p in lst:
            if ans[p-1] < 0:
                que.append(p-1)
                ans[p-1] = ans[q] + 1

    return print(*ans, sep='\n')


if __name__ == '__main__':
    N, M = map(int, input().split())
    R = [[] for _ in range(M)]
    for i in range(M):
        _ = input()
        R[i] = list(map(int, input().split()))

    main()
