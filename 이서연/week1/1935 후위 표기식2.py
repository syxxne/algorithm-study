import sys
import math

input = sys.stdin.readline

N = int(input().strip())

temp = list(map(str, input().strip()))

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

num = []

for _ in range(N):
    num.append(int(input().strip()))

for i in range(len(temp)):
    if temp[i] in alphabet:
        temp[i] = num[alphabet.index(temp[i])]

while len(temp) > 1:
    for i in range(len(temp)):
        if type(temp[i]) == str:
            op = temp.pop(i)
            second = temp.pop(i - 1)
            first = temp.pop(i - 2)

            if op == "+":
                value = first + second
            elif op == "-":
                value = first - second
            elif op == "*":
                value = first * second
            elif op == "/":
                value = first / second

            temp.insert(i - 2, value)

            break

print("{:.2f}".format(math.floor(temp[0] * 100) / 100))
