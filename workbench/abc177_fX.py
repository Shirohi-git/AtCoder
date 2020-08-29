def nextstep(ANS, START, A, B):
    cnt, GOAL = w, set()
    for i in start:
        if A <= i <= B:
            if B < w:
                cnt = min(cnt, B - i + 2)
                GOAL.add(B + 1)
        else:
            cnt = 1
            GOAL.add(i)
    return cnt + ANS, GOAL


h, w = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(h)]

ans, start = 0, set(i for i in range(1, w + 1))
for a, b in ab:
    ans, start = nextstep(ans, start, a, b)
    print(ans if len(start) > 0 else -1)
