def main():
    ans = X // sum(A) * N
    cnt = X // sum(A) * sum(A)
    for ai in A:
        cnt += ai
        ans += 1
        if cnt > X:
            return print(ans)

if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    X = int(input())

    main()
