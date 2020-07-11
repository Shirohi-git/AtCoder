n = int(input())
cnt = [int(input()) for _ in range(5)]

cmax = (n + min(cnt) - 1) // min(cnt)
print(cmax - 1 + 5)
