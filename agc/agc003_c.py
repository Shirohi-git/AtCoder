n = int(input())
a = [int(input()) for _ in range(n)]

evn_a = set(sorted(a)[::2]) ^ set(a[::2])
print(len(evn_a) // 2)
