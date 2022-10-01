def main():
    que = sorted(set(A)) + [INF] * (N - len(set(A)))
    ans, idx = 0, 0
    while len(que) > idx:
        if que[idx] == ans + 1:
            idx += 1
        elif idx <= len(que)-2:
            que.pop(), que.pop()
        else:
            break
        ans += 1
    return print(ans)


if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    INF = 10**10

    main()
