def main():
    ans = sum(max(0, ai-10) for ai in A)
    return print(ans)


if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))

    main()
