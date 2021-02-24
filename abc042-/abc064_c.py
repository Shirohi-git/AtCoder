n = int(input())
a = list(map(int, input().split()))

lst = [0] * 9
for ai in a:
    lst[min(ai, 3200) // 400] += 1
ans = sum(li > 0 for li in lst[:-1])
print(max(ans, 1), ans + lst[-1])
