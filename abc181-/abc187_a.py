a, b = input().split()
a = sum(int(i) for i in a)
b = sum(int(j) for j in b)
print(a if a >= b else b)
