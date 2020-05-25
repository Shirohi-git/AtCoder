x = int(input())

n500, a500 = x // 500, x % 500
n5 = a500//5

print(n500*1000+n5*5)
