def main():
    ans = []
    for i in range(N-K+1):
        for j in range(N-K+1):
            lst = []
            for h in range(K):
                for w in range(K):
                    lst.append(A[i+h][j+w])
            lst = sorted(lst)[::-1]
            ans.append(lst[(K**2) // 2])
    print(ans)
    return None


if __name__ == '__main__':
    N, K = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]

    main()
