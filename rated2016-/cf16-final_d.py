def count(num):
    if num == m - num or num == 0:
        return msum[num] // 2 * 2
    cnt = min(msum[num], msum[m - num])
    for v in xmod[num::m]:
        while cnt + 2 <= msum[num] and v >= 2:
            cnt += 2
            v -= 2
    return cnt


n, m = map(int, input().split())
x = list(map(int, input().split()))

xmod, msum = [0] * (max(x) + 1), [0] * m
for xi in x:
    xmod[xi] += 1
    msum[xi % m] += 1
ans = sum(count(i) for i in range(m))
print(ans // 2)
