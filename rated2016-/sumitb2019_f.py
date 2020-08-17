t1, t2 = map(int, input().split())
a1, a2 = map(int, input().split())
b1, b2 = map(int, input().split())

ave_a = t1 * a1 + t2 * a2
ave_b = t1 * b1 + t2 * b2
if ave_a == ave_b:
    print('infinity')
    exit()

half, all = t1 * (b1 - a1), ave_a - ave_b
ans = half // all * 2 + (half % all != 0)
print(max(0, ans))
