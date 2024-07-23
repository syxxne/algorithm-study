import sys

input = sys.stdin.readline

N, K = map(int, input().split())
S = list(map(int, input().split()))

cnt = 0
end = 0
curr_length = 0
max_length = 0
flag = True

for i in range(N):
    while cnt <= K and flag:
        if S[end] % 2 == 1:
            if cnt == K:
                break

            cnt += 1
        else:
            curr_length += 1

        if end == N - 1:
            flag = False
            break

        end += 1

    max_length = max(max_length, curr_length)

    if S[i] % 2 == 1:
        cnt -= 1
    else:
        curr_length -= 1

print(max_length)
