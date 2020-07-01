n = int(input())
t = [int(input()) for _ in range(n)]

if n <= 2:
    print(max(t))
elif n == 3:
    print(max(sum(t) - max(t), max(t)))
elif n == 4:
    sumt = sum(t)
    cnt1 = min(max(sumt - i, i) for i in t)
    cnt2 = min(max(sumt - t[0] - i, t[0] + i) for i in t[1:])
    print(min(cnt1, cnt2))
