from math import floor as fl

a, b = map(int, input().split())

ans=-1
for i in range(1, 1250):
    if fl(i * 0.08) == a:
        if fl(i * 0.1) == b:
            ans = i
            break

print(ans)
