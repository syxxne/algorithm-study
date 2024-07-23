import sys

input = sys.stdin.readline

N = int(input().strip())

energy = []

for _ in range(N - 1):
    energy.append(list(map(int, input().split())))

K = int(input().strip())

if N == 1:
    print(0)
    sys.exit()

dp = [[1e9] * 2 for _ in range(N)]
dp[0][0] = 0
dp[1][0] = energy[0][0]


for i in range(2, N):
    dp[i][0] = min(dp[i - 1][0] + energy[i - 1][0], dp[i - 2][0] + energy[i - 2][1])

    if i >= 3:
        dp[i][1] = min(dp[i - 1][1] + energy[i - 1][0], dp[i - 2][1] + energy[i - 2][1], dp[i - 3][0] + K)


print(min(dp[-1]))