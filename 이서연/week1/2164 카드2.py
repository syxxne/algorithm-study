import sys
from collections import deque

input = sys.stdin.readline

N = int(input().strip())

cards = deque()

for i in range(1, N + 1):
    cards.append(i)

while True:
    if len(cards) == 1:
        break

    cards.popleft()
    cards.append(cards.popleft())

print(cards[0])