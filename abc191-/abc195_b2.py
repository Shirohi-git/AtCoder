a, b, w = map(int, input().split())

s, l = (w * 1000 + b - 1) // b, w * 1000 // a
print(*[s, l] if l >= s else['UNSATISFIABLE'])
