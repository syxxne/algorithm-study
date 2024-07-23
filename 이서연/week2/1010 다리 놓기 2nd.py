import sys
import math

input = sys.stdin.readline

# 조합 풀이
#
# T = int(input().strip())
#
# for _ in range(T):
#     N, M = map(int, input().split())
#
#     if N == M:
#         print(1)
#     else:
#         print(math.comb(M, N))


# dp 풀이

T = int(input().strip())

for _ in range(T):
    N, M = map(int, input().split())

    if N == M:
        print(1)
    elif N == 1:
        print(M)
    else:
        dp = [[0] * (M + 1) for _ in range(N + 1)]

        for i in range(1, M + 1):
            dp[1][i] = i

        for i in range(2, N + 1):
            for j in range(i, M + 1):
                for k in range(j - 1, i - 2, -1):
                    dp[i][j] += dp[i - 1][k]

        print(dp[N][M])