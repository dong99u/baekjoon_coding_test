ORIGINAL = 1000

n = int(input())

TARGET = ORIGINAL - n

count = 0
while TARGET >= 500:
    TARGET -= 500
    count += 1

while TARGET >= 100:
    TARGET -= 100
    count += 1

while TARGET >= 50:
    TARGET -= 50
    count += 1

while TARGET >= 10:
    TARGET -= 10
    count += 1

while TARGET >= 5:
    TARGET -= 5
    count += 1

while TARGET >= 1:
    TARGET -= 1
    count += 1

print(count)

