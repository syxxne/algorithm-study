n, m = map(int, input().split())

dp = [[0 for i in range(101)]for j in range(101)]

for i in range(1, n+1):
    dp[i][0] = 1
    dp[i][i] = 1
    
for i in range(2, n+1):
    for j in range(1, m+1):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

print(dp[n][m])
        