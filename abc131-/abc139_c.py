n = int(input())
h = list(map(int, input().split()))
cnt = 0
ans = []
for i in range(1, n):
    if h[i-1] >= h[i]:
        cnt += 1
    else:
        ans.append(cnt)
        cnt = 0
ans.append(cnt)
print(max(ans))
