n = int(input())
a = sorted(map(int, input().split()))[::-1]
print(sum(a[1:2 * n:2]))
