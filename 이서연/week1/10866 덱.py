import sys
from collections import deque

input = sys.stdin.readline

N = int(input().strip())

queue = deque()

for _ in range(N):
    command = input().strip()

    if 'push_front' in command:
        queue.appendleft(command.split()[-1])
    elif 'push_back' in command:
        queue.append(command.split()[-1])
    elif 'pop_front' in command:
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif 'pop_back' in command:
        if queue:
            print(queue.pop())
        else:
            print(-1)
    elif 'size' in command:
        print(len(queue))
    elif 'empty' in command:
        if queue:
            print(0)
        else:
            print(1)
    elif 'front' in command:
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif 'back' in command:
        if queue:
            print(queue[-1])
        else:
            print(-1)