def main():
    cnt = [0]
    for si in S:
        cnt.append(cnt[-1] + (si == '.'))

    l, ans = 0, 0
    for i, ci in enumerate(cnt):
        if ci - cnt[l] > K:
            l += 1
        ans = max(ans, i-l)
    return print(ans)


if __name__ == '__main__':
    S = input()
    K = int(input())

    main()
