s = int(input())

div, mod = divmod(s, 10 ** 9)
ans = [0, 0, 10 ** 9, 1, 0, div]
if mod != 0:
    ans[4:] = [10 ** 9 - mod, div + 1]
print(*ans)
