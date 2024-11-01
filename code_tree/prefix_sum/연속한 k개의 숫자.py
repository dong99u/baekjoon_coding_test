import sys

input = sys.stdin.readline

n, k, b = map(int, input().split())

arr = []

for _ in range(b):
    arr.append(int(input()))