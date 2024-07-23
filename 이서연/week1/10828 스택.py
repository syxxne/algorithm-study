import sys

input = sys.stdin.readline

N = int(input().strip())

stack = []
result = []

for _ in range(N):
    temp = list(map(str, input().split()))

    if temp[0] == 'push':
        stack.append(int(temp[1]))
    elif temp[0] == 'pop':
        if len(stack) == 0:
            result.append(-1)
        else:
            result.append(stack.pop(-1))
    elif temp[0] == 'size':
        result.append(len(stack))
    elif temp[0] == 'empty':
        if len(stack) == 0:
            result.append(1)
        else:
            result.append(0)
    elif temp[0] == 'top':
        if len(stack) == 0:
            result.append(-1)
        else:
            result.append(stack[-1])

for i in result:
    print(i)
