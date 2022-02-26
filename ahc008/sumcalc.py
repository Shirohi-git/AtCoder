def main():
    lst = [input() for _ in range(4 * N)][2::4]
    lst = [*map(lambda x:int(x.split()[2]), lst)]
    return print(sum(lst))


if __name__ == "__main__":
    N = 100
    # N = int(input('N -> '))
    main()


