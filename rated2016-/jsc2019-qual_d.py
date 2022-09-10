def main():
    ans = [[] for _ in range(N-1)]
    for i in range(1, N+1):
        for j in range(1, i):
            sft = 0
            while (i ^ j) >> sft:
                if ((i ^ j) >> sft) & 1:
                    ans[j-1].append(sft+1)
                    break
                sft += 1
    for ai in ans:
        print(*ai)
    return


if __name__ == '__main__':
    N = int(input())

    main()
