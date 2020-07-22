n = int(input())
b = list(map(int, input().split()))

ans = []
for _ in range(n):
    for i, bi in enumerate(b[::-1]):
        i = len(b) - i
        if i == bi:
            ans.append(b.pop(i - 1))
            break
print(*(ans[::-1] if len(ans) == n else[-1]), sep='\n')
