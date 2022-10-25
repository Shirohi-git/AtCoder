def main():
    ans = [-1] * (2*N+2)
    ans[1] = 0
    for i, ai in enumerate(A, 1):
        ans[2*i] = ans[2*i+1] = ans[ai]+1
    return print(*ans[1:], sep='\n')


if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))

    main()
