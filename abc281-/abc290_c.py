def main():
    ans = 0
    for ai in A[:K]:
        if ans == ai:
            ans += 1
    return print(ans)


if __name__ == '__main__':
    N, K = map(int, input().split())
    A = sorted(set(map(int, input().split())))

    main()
