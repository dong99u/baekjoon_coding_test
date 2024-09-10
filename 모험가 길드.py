import sys
input = sys.stdin.readline

n = int(input())

input_list = list(map(int, input().split()))
input_list.sort()

answer = 0
count = 0

for i in input_list:
    count += 1

    if count >= i:
        answer += 1
        count = 0

print(answer)


