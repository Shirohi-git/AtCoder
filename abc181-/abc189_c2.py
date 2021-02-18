n = int(input())
a = list(map(int, input().split())) + [0]

# 解説AC O(N)
ans = 0
stack = [(-1, 0)]
for r, ai in enumerate(a):
    while stack[-1][1] > ai:
        _, x = stack.pop()
        l = stack[-1][0]
        ans = max(ans, x * (r - 1 - l))
    stack.append((r, ai))
print(ans)
