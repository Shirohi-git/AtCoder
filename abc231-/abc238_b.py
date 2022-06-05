def main():
    ans = [360]
    idx = 0
    for ai in A:
        now = ai
        while ans[idx] < now:
            now -= ans[idx]
            idx = (idx+1) % len(ans)
        ans.insert(idx+1, ans[idx]-now)
        ans[idx] = now
        idx = (idx+1) % len(ans)
    return print(max(ans))


if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))

    main()