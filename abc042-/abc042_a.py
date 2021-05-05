abc = list(map(int, input().split()))

res = (abc.count(5) == 2 and abc.count(7))
print('YES' if res else 'NO')
