def main():
    def add2(num):
        if num <= W:
            ans.add(num)
        return

    ans = set()
    for i in range(N):
        add2(A[i])
        for j in range(i+1, N):
            add2(A[i]+A[j])
            for k in range(j+1, N):
                add2(A[i]+A[j]+A[k])
    return print(len(ans))


if __name__ == '__main__':
    N, W = map(int, input().split())
    A = list(map(int, input().split()))

    main()
