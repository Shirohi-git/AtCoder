def main():
    ans = 0
    for _ in range(3):
        ans = A[ans]
    return print(ans)


if __name__ == '__main__':
    A = list(map(int, input().split()))

    main()
