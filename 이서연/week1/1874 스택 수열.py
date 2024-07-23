import sys
from collections import deque

input = sys.stdin.readline

n = int(input().strip())

stack = deque()
num = 1
result = []

for _ in range(n):
    target = int(input().strip())

    while num <= target:
        stack.append(num)
        result.append("+")
        num += 1

    if stack[-1] == target:
        stack.pop()
        result.append("-")
    else:
        print("NO")
        sys.exit()

for i in result:
    print(i)