import sys

input = sys.stdin.readline

expression = str(input().strip())

cnt = 0
result = 0

for i in range(len(expression) - 1):
    if expression[i] == '(' and expression[i + 1] == '(':
        cnt += 1
        result += 1
    elif expression[i] == '(' and expression[i + 1] == ')':
        result += cnt
    elif expression[i] == ')' and expression[i + 1] == ')':
        cnt -= 1

print(result)