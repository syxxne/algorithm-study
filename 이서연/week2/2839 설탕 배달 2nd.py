import sys

input = sys.stdin.readline

N = int(input().strip())

if N == 3 or N == 5:
    print(1)
elif N < 5:
    print(-1)
else:
    dp = [1e9] * (N + 1)

    dp[3] = 1
    dp[5] = 1

    for i in range(6, N + 1):
        value = min(dp[i - 5], dp[i - 3])

        if value != 1e9:
            dp[i] = value + 1

    if dp[N] < 1e9:
        print(dp[N])
    else:
        print(-1)