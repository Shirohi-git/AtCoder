w, h = map(int, input().split())
p = sorted([int(input()) for _ in range(w)] + [1e9])[::-1]
q = sorted([int(input()) for _ in range(h)] + [1e9])[::-1]

# 解説AC
ans = 0
cnt = [h+1, w+1]
while len(p)-1 or len(q)-1:
    tmp = (p[-1] < q[-1])
    cost = p.pop() if tmp else q.pop()
    ans += cost * cnt[1-tmp]
    cnt[tmp] -= 1
print(ans)
