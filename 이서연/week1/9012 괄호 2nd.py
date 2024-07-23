import sys

input = sys.stdin.readline

N = int(input().strip())

for _ in range(N):
    PS = []
    test = str(input().strip())

    for i in test:
        if PS and PS[-1] == '(' and i == ')':
            PS.pop(-1)
        else:
            PS.append(i)

    if PS:
        print("NO")
    else:
        print("YES")