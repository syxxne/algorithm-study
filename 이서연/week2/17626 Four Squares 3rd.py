import sys

input = sys.stdin.readline

n = int(input().strip())

# dp, Pypy (파이썬은 시간 초과)
#
# if n == 1:
#     print(1)
# else:
#     dp = [0] * (n + 1)
#     dp[1] = 1
#
#     for i in range(2, n + 1):
#         square = int(i ** (1 / 2))
#
#         if i == square ** 2:
#             dp[i] = 1
#         elif i - 1 == square ** 2:
#             dp[i] = 2
#         else:
#             cnt = 1e9
#
#             for j in range(1, square + 1):
#                 cnt = min(cnt, dp[i - (j ** 2)])
#
#             dp[i] = cnt + 1
#
#     print(dp[n])

# 브루트포스, 파이썬

is_sqaure = [False] * (n + 1)

i = 1

while i ** 2 <= n:
    is_sqaure[i ** 2] = True
    i += 1

if is_sqaure[n]:
    print(1)
else:
    first_square = int(n ** 0.5)

    cnt = 4

    for i in range(first_square, 0, -1):
        if is_sqaure[n - (i ** 2)]:
            cnt = 2
            break
        else:
            second_sqaure = int((n - i ** 2) ** 0.5)

            for j in range(second_sqaure, 0, -1):
                if is_sqaure[n - (i ** 2) - (j ** 2)]:
                    cnt = 3

    print(cnt)