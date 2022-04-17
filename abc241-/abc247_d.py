from collections import deque


def main():
    num_cnt = deque([])
    query = [(qi+[0])[:3] for qi in Query]
    for t, x, c in query:
        if t == 1:
            num_cnt.append((x, c))
        if t == 2:
            ans = 0
            while x > 0:
                tx, tc = num_cnt.popleft()
                ans += tx * min(x, tc)
                tc, x = tc-min(x, tc), x-min(x, tc)
                if tc > 0:
                    num_cnt.appendleft((tx, tc))
            print(ans)
    return


if __name__ == '__main__':
    Q = int(input())
    Query = [list(map(int, input().split())) for _ in range(Q)]

    main()
