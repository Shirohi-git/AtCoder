def main():
    ans = (A-1+K) % N
    return print(ans if ans else N)


if __name__ == '__main__':
    N, K, A = map(int, input().split())

    main()
