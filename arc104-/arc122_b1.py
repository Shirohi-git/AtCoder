def main():
    x = A[N//2]
    ans = sum(ai + abs(ai-x) for ai in A) / 2
    return print(ans / N)


if __name__ == '__main__':
    N = int(input())
    A = sorted(map(int, input().split()))[::-1]

    main()
