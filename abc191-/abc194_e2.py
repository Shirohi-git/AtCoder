n, m = map(int, input().split())
a = list(map(int, input().split()))

# 解説AC O(n) ver.1
flag = [0] * (max(a) + 2)
for ai in a[:m]:
    flag[ai] += 1

ans = flag.index(0)
for out, add in zip(a[:-m], a[m:]):
    flag[out] -= 1
    flag[add] += 1
    if flag[out] == 0:
        ans = min(out, ans)
print(ans)
