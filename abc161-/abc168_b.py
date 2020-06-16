k = int(input())
s = str(input())

print(s if k >= len(s) else s[:k]+'...')
