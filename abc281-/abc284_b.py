def main():
    ans = sum(ai % 2 for ai in A)
    return print(ans)


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N, A = int(input()), list(map(int, input().split()))

        main()