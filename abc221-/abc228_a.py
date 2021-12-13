def main():
    res = (S <= X < T)
    if S > T:
        res |= (S <= X < 24 or 0 <= X < T)
    return print("Yes" if res else "No")


if __name__ == '__main__':
    S, T, X = map(int, input().split())

    main()
