def main():
    ans = 0
    stack = [(A[i], i, 1) for i in range(N-4)]
    while stack:
        mod, idx, cnt = stack.pop()
        if cnt == 5:
            ans += (mod == Q)
            continue
        for j in range(idx+1, N-4 + cnt):
            nxt = (mod * A[j]) % P
            stack.append((nxt, j, cnt+1))
    return print(ans)


if __name__ == '__main__':
    N, P, Q = map(int, input().split())
    A = list(map(lambda x: int(x) % P, input().split()))

    main()
