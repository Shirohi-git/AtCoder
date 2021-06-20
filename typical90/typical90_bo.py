def main():
    num8 = N
    for _ in range(int(K)):
        num10 = int(num8, 8)
        if num10 == 0:
            num8 = "0"
            continue

        num8 = ""
        while num10:
            num8 = str(num10 % 9) + num8
            num10 //= 9
        num8 = num8.replace('8', '5')
    return print(num8)


if __name__ == '__main__':
    N, K = input().split()

    main()
