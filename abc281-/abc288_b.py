def main():
    return print(*sorted(A[:K]), sep='\n')


if __name__ == '__main__':
    N, K = map(int, input().split())
    A = [input() for _ in range(N)]

    main()