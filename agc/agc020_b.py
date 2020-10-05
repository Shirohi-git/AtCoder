k = int(input())
a = list(map(int, input().split()))

l, r, res = 2, 3, (a[-1] == 2)
for ai in a[::-1]:
    if (r - l < ai) and (0 < l % ai < r % ai):
        res = False
    l = (l + ai - 1) // ai * ai
    r = r // ai * ai + (ai - 1)
print(*((l, r) if res else [-1]))
