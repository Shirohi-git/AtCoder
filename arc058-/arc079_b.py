def main():
    print(50)
    div, mod = divmod(K, 50)
    a = [50 + div] * mod
    a += [49 - mod + div] * (50 - mod)
    return print(*a)


if __name__ == '__main__':
    K = int(input())

    main()
