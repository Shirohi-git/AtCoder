def main():
    ma = max(A)
    ans =  max(ai for ai in A if ai != ma)
    return print(ans)


if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))

    main()
