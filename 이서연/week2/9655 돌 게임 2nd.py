import sys

input = sys.stdin.readline

N = int(input().strip())

dp = [0] * (N + 1)

for i in range(1, N + 1):
    if i % 3 == 0:
        dp[i] = dp[i - 3] + 1
    else:
        dp[i] = dp[i - 1] + 1


if dp[N] % 2 == 0:
    print("CY")
else:
    print("SK")