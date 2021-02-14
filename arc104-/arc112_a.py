t = int(input())
lr = [list(map(int, input().split())) for _ in range(t)]

for l, r in lr:
    num = max(r - l * 2, -1) + 2
    print(num * (num - 1) // 2)
