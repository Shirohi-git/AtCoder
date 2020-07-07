n = int(input())
a = list(map(int, input().split()))

ave = sum(a)//n
ans1 = sum((ai - ave) ** 2 for ai in a)
ans2 = sum((ai - ave - 1) ** 2 for ai in a)
print(min(ans1,ans2))
