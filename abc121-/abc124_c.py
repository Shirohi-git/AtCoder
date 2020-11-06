s = input()

cnt1 = sum(str(i % 2) != si for i, si in enumerate(s))
cnt2 = sum(str(1 - i % 2) != si for i, si in enumerate(s))
print(min(cnt1, cnt2))
