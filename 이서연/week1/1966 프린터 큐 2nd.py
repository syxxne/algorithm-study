import sys
from collections import deque

input = sys.stdin.readline

test_num = int(input().strip())

for _ in range(test_num):
    N, M = map(int, input().split())
    temp = list(map(int, input().strip().split()))

    if N == 1:
        print(1)
    else:
        importance = deque()

        for i in range(N):
            if i == M:
                importance.append(("target", temp[i]))
            else:
                importance.append(("N", temp[i]))

        cnt = 1

        while True:
            if max(importance, key=lambda x:x[1])[1] == importance[0][1]:
                if importance[0][0] == "target":
                    print(cnt)
                    break
                else:
                    importance.popleft()
                    cnt += 1
            else:
                importance.append(importance.popleft())

