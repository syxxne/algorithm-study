import sys

input = sys.stdin.readline

T = int(input().strip())

numbers = []

for _ in range(T):
    n = int(input().strip())
    numbers.append(n)

dp = [0] * (max(numbers) + 1)

dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, len(dp)):
    dp[i] = dp[i - 3] + dp[i - 2] + dp[i - 1]

for i in numbers:
    print(dp[i])