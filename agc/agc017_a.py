n, p = map(int, input().split())
a = list(map(int, input().split()))

odd = [i for i in a if i % 2 == 1]
even = [i for i in a if i % 2 == 0]
ecnt = pow(2, len(even))
ocnt = pow(2, max(len(odd)-1,0))
print(0 if (len(odd) == 0 and p == 1) else ecnt * ocnt)
