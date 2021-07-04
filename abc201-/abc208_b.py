def main():
    p = P
    coin = [1]
    for i in range(2, 11):
        coin.append(coin[-1]*i)

    ans = 0
    for ci in coin[::-1]:
        div, p = divmod(p, ci)
        ans += div
    return print(ans)


if __name__ == '__main__':
    P = int(input())

    main()
