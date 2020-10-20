n = int(input())
a = len(set(input().split()))
print(a - (n - a) % 2)
