def main():
    from heapq import heappush, heappop

    def solve(lst):
        nxt = 1
        que = []
        while lst or que:
            if not que:
                nxt = lst[-1][0]
            while lst and lst[-1][0] == nxt:
                heappush(que, lst.pop()[1])
            if nxt > heappop(que):
                return False
            nxt += 1
        return True

    for lr in test:
        ans = solve(lr)
        print('Yes' if ans else 'No')
    return


if __name__ == '__main__':
    T = int(input())
    test = []
    for ti in range(T):
        n = int(input())
        ti_lr = [tuple(map(int, input().split())) for _ in range(n)]
        test.append(sorted(ti_lr)[::-1])

    main()
