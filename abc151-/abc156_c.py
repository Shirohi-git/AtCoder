n = int(input())
x = list(map(int, input().split()))

ave = sum(x) // n
ans1 = sum((xi - ave)**2 for xi in x)
ans2 = sum((xi - ave - 1)**2 for xi in x)
print(min(ans1, ans2))

if n == 2:
    print(n)
