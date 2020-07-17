def ceil(X, Y):  # 天井関数 ceil(X/Y) Y>1
    return (X + Y - 1) // Y


n = int(input())
ta = [list(map(int, input().split())) for _ in range(n)]

t, a = 1, 1
for ti, ai in ta:
    tmp = max(ceil(t, ti), ceil(a, ai))
    t, a = ti * tmp, ai * tmp
print(t + a)
