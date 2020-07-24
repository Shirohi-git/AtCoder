n = int(input())
b = list(map(int, input().split()))

ans = []
for _ in range(n):
    for i, bi in enumerate(b[::-1]):
        if len(b) == bi + i:
            ans.append(b.pop(len(b) - i - 1))
            break
print(*(ans[::-1] if len(ans) == n else [-1]), sep='\n')
