from statistics import median_high, median_low

n = int(input())
l = list(map(int, input().split()))

a, b = median_low(l), median_high(l)
for i in l:
    if i <= a:
        print(b)
    else:
        print(a)
