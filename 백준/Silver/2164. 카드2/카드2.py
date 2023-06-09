from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

cards = deque([i for i in range(1, n+1)])

while len(cards) != 1:
    cards.popleft()
    temp = cards.popleft()
    cards.append(temp)

print(cards[0])