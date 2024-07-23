import sys

input = sys.stdin.readline

N = int(input().strip())

points = [0]

for _ in range(N):
    points.append(int(input().strip()))

if N == 1:
    print(points[1])
elif N == 2:
    print(points[1] + points[2])
else:
    dp = [0] * (N + 1)
    dp[1] = points[1]
    dp[2] = points[1] + points[2]

    cnt = 2

    for i in range(3, N + 1):
        if cnt == 2:
            if dp[i - 2] >= dp[i - 3] + points[i - 1]:
                cnt = 1
                dp[i] = dp[i - 2] + points[i]
            else:
                dp[i] = dp[i - 3] + points[i - 1] + points[i]
        else:
            if dp[i - 2] >= dp[i - 1]:
                dp[i] = dp[i - 2] + points[i]
            else:
                cnt = 2
                dp[i] = dp[i - 1] + points[i]

    print(dp[N])