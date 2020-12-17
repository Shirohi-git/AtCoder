n = int(input())
a = list(map(int, input().split()))
print(sum(ai - 1 for ai in a))
