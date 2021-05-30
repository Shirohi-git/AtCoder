def main():
    ans = sum(i*100 + j for j in range(1, K+1) for i in range(1, N+1))
    return print(ans)


if __name__ == '__main__':
    N, K = map(int, input().split())
    main()
