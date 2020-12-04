m = int(input())
dc = [list(map(int, input().split())) for _ in range(m)]

digit = sum(c for _, c in dc)
num = sum(d * c for d, c in dc)
ans = (digit - 1) + num // 9 - (num % 9 == 0)
print(ans)
