s = input()
res = (s[0] == s[-1]) ^ (len(s) % 2)
print("First" if res else "Second")
