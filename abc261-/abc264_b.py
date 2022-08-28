def main():
    res = 1
    TB = [*map(tuple, zip(range(15),range(15)[::-1]))]
    for tb in TB:
        if R-1 in tb or C-1 in tb:
            break
        res ^= 1
    return print("black" if res else "white")


if __name__ == '__main__':
    R, C = map(int, input().split())

    main()
