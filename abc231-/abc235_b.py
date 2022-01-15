def main():
    ans = 0
    for hi in H:
        if hi > ans:
            ans = hi
            continue
        break
    return print(ans)


if __name__ == '__main__':
    N = int(input())
    H = list(map(int, input().split()))

    main()
