import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


turn, time = map(int, input().split())
if turn == 0:
    print(time, 0)
    sys.exit(0)
info = deque([input().split() for i in range(turn)])
diff = deque([int(info[i][0]) - int(info[i - 1][0]) for i in range(1, turn)])
diff.append(time - int(info[-1][0]))
x, y = int(info[0][0]), 0
oldFlag = "+x"
for _ in range(turn):
    j = info.popleft()[1]
    if j == "right":
        if oldFlag == "+x":
            newFlag = "-y"
        if oldFlag == "-y":
            newFlag = "-x"
        if oldFlag == "-x":
            newFlag = "+y"
        if oldFlag == "+y":
            newFlag = "+x"
    if j == "left":
        if oldFlag == "+x":
            newFlag = "+y"
        if oldFlag == "+y":
            newFlag = "-x"
        if oldFlag == "-x":
            newFlag = "-y"
        if oldFlag == "-y":
            newFlag = "+x"
    i = diff.popleft()
    if newFlag == "+x":
        x += i
    if newFlag == "-x":
        x -= i
    if newFlag == "+y":
        y += i
    if newFlag == "-y":
        y -= i
    oldFlag = newFlag
    newFlag = None
print(x, y)
