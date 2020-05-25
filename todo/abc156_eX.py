import sys
input = sys.stdin.readline


n = int(input())
n, k = map(int, input().split())
a = list(map(int, input().split()))
ab = [list(map(int, input().split())) for _ in range(n)]
