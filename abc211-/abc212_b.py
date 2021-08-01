def main():
    res = any((N[i]+1) % 10 != N[i+1] for i in range(3))
    res &= (len(set(N)) > 1)
    return print("Strong" if res else "Weak")


if __name__ == '__main__':
    N = list(map(int, input()))

    main()
