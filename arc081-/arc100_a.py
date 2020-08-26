from statistics import median_low

n = int(input())
a = list(map(int, input().split()))

a = [ai - i for i, ai in enumerate(a)]
med = median_low(a)
print(sum(abs(ai - med) for ai in a))
