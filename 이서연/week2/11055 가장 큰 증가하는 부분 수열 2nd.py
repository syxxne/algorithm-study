import sys

input = sys.stdin.readline

N = int(input().strip())
numbers = list(map(int, input().split()))

dp = [0] * N
dp[0] = numbers[0]

for i in range(1, N):
    for j in range(i):
        if numbers[j] < numbers[i]:
            dp[i] = max(dp[i], dp[j])

    dp[i] += numbers[i]

print(max(dp))
