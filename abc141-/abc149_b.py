a, b, k = map(int, input().split())

a_ans = max(a - k, 0)
b_ans = max(b - max(k - a, 0), 0)
print(a_ans, b_ans)
