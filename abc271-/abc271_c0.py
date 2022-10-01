from collections import deque, Counter


def main():
    que = deque(sorted(set(A)))
    sell = sum(ci-1 for ci in Counter(A).values())
    ans = 0
    while sell or que:
        if que:
            top = que.popleft()
            if top == ans+1:
                sell += 2
            else:
                que.appendleft(top)

        while que:
            nxt = que.popleft()
            if nxt <= ans:
                sell += 1
            else:
                que.appendleft(nxt)
                break
        
        if sell + len(que) > 1:
            ans += 1
            for _ in range(2):
                if sell:
                    sell -= 1
                else:
                    que.pop()
        else:
            break
    return print(ans)


if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))

    main()
