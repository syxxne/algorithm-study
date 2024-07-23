t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    dp = [[0]*(m+1) for _ in range(m+1)]
    
    for a in range(1, n+1):
        for b in range(1, m+1):
            if a == 1:
                dp[a][b] = b
            
            elif a == b:
                dp[a][b] = 1
            
            else:
                if b>a:
                    dp[a][b] = dp[a][b-1] + dp[a-1][b-1]
            
    print(dp[n][m])

    