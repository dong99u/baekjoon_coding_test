import sys
input = sys.stdin.readline

INF = float('inf')
n, m = map(int, input().split())

A = list(map(int, input().split()))

dp = [INF] * n


