import sys
from collections import deque
def input(): return sys.stdin.readline().rstrip()


def findTomato(lst):
    coord = []
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            for k in range(len(lst[i][j])):
                if lst[i][j][k] == 1:
                    coord.append([i, j, k])
    return coord


def isSuccess(lst):
    for i in lst:
        for j in i:
            for k in j:
                if k == 0:
                    return False
    return True


col, row, height = map(int, input().split())
top = []
for h in range(height):
    box = []
    for r in range(row):
        box.append(list(map(int, input().split())))  # col
    top.append(box)
dx = [0, 0, 0, 0, 1, -1]
dy = [0, 0, 1, -1, 0, 0]
dz = [1, -1, 0, 0, 0, 0]

whereisone = findTomato(top)
queue = deque([])
for i in whereisone:
    queue.append(i)
day = 0
l = len(queue)
while queue:
    for i in range(l):
        p = queue.popleft()
        if top[p[0]][p[1]][p[2]] == 1:
            for i in range(6):
                if 0 <= p[2] + dx[i] < col and 0 <= p[1] + dy[i] < row and 0 <= p[0] + dz[i] < height:
                    new_x = p[2] + dx[i]
                    new_y = p[1] + dy[i]
                    new_z = p[0] + dz[i]
                    if top[new_z][new_y][new_x] == 0:
                        top[new_z][new_y][new_x] = 1
                        queue.append([new_z, new_y, new_x])
    l = len(queue)
    day += 1

# 5 3 1
# 0 0 0 0 0
# 0 1 0 1 0
# 0 0 0 0 0

if isSuccess(top):
    print(day - 1)
else:
    print(-1)
