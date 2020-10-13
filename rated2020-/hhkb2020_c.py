n = int(input())
p = list(map(int, input().split()))

ans = 0
flag = [0] * (max(p) + 2)
for pi in p:
    flag[pi] += 1
    while flag[ans] > 0:
        ans += 1
    print(ans)
