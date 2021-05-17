n = int(input())
s, t = input(), input()

plc_s = [i for i in range(n) if s[i] == '0']
plc_t = [i for i in range(n) if t[i] == '0']
ans = sum(si != ti for si, ti in zip(plc_s, plc_t))
print(ans if len(plc_s) == len(plc_t) else -1)
