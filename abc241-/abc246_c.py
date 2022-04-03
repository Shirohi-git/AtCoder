def main():
    ans, k = 0, K
    mod = []
    for ai in A:
        c = ai // X
        ai -= min(c, k) * X
        k -= min(c, k)
        ans += ai 
        mod.append(ai)
    if k:
        ans -= sum(sorted(mod)[-k:])
    return print(ans)


if __name__ == '__main__':
    N, K, X = map(int, input().split())
    A = sorted(map(int, input().split()))[::-1]

    main()
