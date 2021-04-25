n = int(input())
a = max(map(int, input().split()))
b = min(map(int, input().split()))

print(max(b - a + 1, 0))
