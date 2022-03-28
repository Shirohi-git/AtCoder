def main():
    ans = 0
    for ai in A:
        if ans == ai:
            ans += 1
    return print(ans)


if __name__ == '__main__':
    N = int(input())
    A = sorted(set(map(int, input().split())))

    main()
