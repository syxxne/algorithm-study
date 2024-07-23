n = int(input())

count = 0

dp = [5001] * max(6, n+1)

dp[3] = 1
dp[5] = 1

for i in range(6, n+1):
    dp[i] = min(dp[i-3], dp[i-5]) + 1
    

if dp[n] != 5001:
    print(dp[n])
else:
    print(-1)
