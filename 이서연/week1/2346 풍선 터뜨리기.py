import sys

input = sys.stdin.readline

N = int(input().strip())

temp = list(map(int, input().split()))

balloons = []

for i in range(N):
    balloons.append((i + 1, temp[i]))

result = []
idx = 0

while len(balloons) > 1:
    num, paper = balloons.pop(idx)
    result.append(num)

    if paper > 0:
        idx = (idx + paper - 1) % len(balloons)
    else:
        idx = (idx + paper) % len(balloons)

result.append(balloons[0][0])

print(*result)