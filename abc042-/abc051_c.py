sx, sy, tx, ty = map(int, input().split())

ans = 'R' * (tx - sx) + 'U' * (ty - sy)
ans += 'L' * (tx - sx) + 'D' * (ty - sy)
ans += 'L' + 'U' * (ty - sy + 1) + 'R' * (tx - sx + 1) + 'D'
ans += 'R' + 'D' * (ty - sy + 1) + 'L' * (tx - sx + 1) + 'U'
print(ans)
