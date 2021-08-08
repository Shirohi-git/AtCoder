def main():
    ans = sorted(range(1,N+1), key=lambda x:A[x-1])[-2]
    return print(ans)


if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))

    main()
