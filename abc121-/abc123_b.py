from itertools import permutations

dish = [int(input()) for _ in range(5)]

ans = 1000
for p in permutations(dish):
    t = 0
    for pi in p:
        t = (t + 9) // 10 * 10 + pi
    ans = min(ans, t)
print(ans)
