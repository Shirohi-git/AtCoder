h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]

mina = min(min(ai) for ai in a)
print(sum(sum(aij - mina for aij in ai) for ai in a))
