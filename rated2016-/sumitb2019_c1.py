x = int(input())

#解説ver
cnt = x // 100
print(1 if 100 * cnt <= x <= 105 * cnt else 0)
