n, s, t = int(input()), input(), input()

lst = [i for i in range(n + 1) if s[-i:] == t[:i]]
print(2 * n - max(lst + [0]))
