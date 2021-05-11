n = int(input())
a = [int(input()) for _ in range(n)]

ans, cost = a[0]-1, 2
for ai in a[1:]:
    ans += (ai-1) // cost
    cost += (ai == cost)
print(ans)
