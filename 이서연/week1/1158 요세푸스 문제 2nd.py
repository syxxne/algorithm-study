import sys

input = sys.stdin.readline

N, K = map(int, input().split())

people = []

for i in range(1, N + 1):
    people.append(i)

result = []

idx = K - 1
result.append(people.pop(idx))

while people:
    idx = (idx + (K - 1)) % len(people)
    result.append(people.pop(idx))

print("<", end="")

for i in range(N):
    if i == N - 1:
        print(result[i], end=">")
    else:
        print(result[i], end=", ")