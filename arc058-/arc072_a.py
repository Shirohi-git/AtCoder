def solve(ini_val):
    acc, cnt = 0, 0
    for ai in a:
        acc += ai
        if acc * ini_val < 1:
            cnt += abs(ini_val - acc)
            acc += ini_val - acc
        ini_val *= -1
    return cnt

n = int(input())
a = list(map(int, input().split()))
print(min(solve(1), solve(-1)))
