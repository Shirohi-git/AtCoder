n, k = map(int, input().split())
a = sorted(map(int, input().split()))

ans = [0] * k
cnt = 0
for ai in a:
    if cnt == k or ans[cnt] != ai:
        cnt = 0
    if ans[cnt] == ai:
        ans[cnt] += 1
        cnt += 1
print(sum(ans))
