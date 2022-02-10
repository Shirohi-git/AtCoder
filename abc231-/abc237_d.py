from collections import deque


def main():
    ans = deque([N])
    for i, si in enumerate(S[::-1]):
        if si == 'L':
            ans.append(N-1-i)
        if si == 'R':
            ans.appendleft(N-1-i)
    return print(*ans)


if __name__ == '__main__':
    N = int(input())
    S = input()

    main()
