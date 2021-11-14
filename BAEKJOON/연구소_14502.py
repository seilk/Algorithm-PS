import sys
import copy
from itertools import combinations
from collections import deque
def input(): return sys.stdin.readline().rstrip()


def findVirus(lab):
    whereVirus = []
    for i in range(len(lab)):
        for j in range(len(lab[i])):
            if lab[i][j] == 2:
                whereVirus.append([i, j])
    return whereVirus


def findSecure(lab):
    cnt = 0
    for i in lab:
        cnt += i.count(0)
    return cnt


def findCanWall(lab):
    coord = []
    for i in range(len(lab)):
        for j in range(len(lab[i])):
            if lab[i][j] == 0:
                coord.append([i, j])
    return coord


# def DFS(depth, visited, zeros, coordSet, tmp):
#     if depth == 3:
#         coordSet.add(tuple(tmp))
#         return
#     for i in range(len(zeros)):
#         if not visited[i]:
#             item = (zeros[i][0], zeros[i][1])
#             visited[i] = 1
#             tmp.append(item)
#             DFS(depth + 1, visited, zeros, coordSet, tmp)
#             tmp.discard(item)
    # visited[i] = 0
#


n, m = map(int, input().split())
lab_og = [list(map(int, input().split())) for i in range(n)]
#

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
lab_copy = copy.deepcopy(lab_og)
zeros = findCanWall(lab_og)
coordSet = list(combinations(zeros, 3))
# DFS(0, visited, zeros, coordSet, [])  # find 3 walls coordination
visited = [[[0] * n] for i in range(n)]

seT = []
for i in range():
    for j in range():
        visited[i][j] = 1
        seT.append([i, j])
for i in range()
   for j in range()
       if visited[i][j] != 1:
            visited[i][j] = 1
        seT.append([i, j])

viruses = findVirus(lab_og)
answer = 0
for coord in coordSet:
    visited = [[0] * m for i in range(n)]
    lab_copy[coord[0][0]][coord[0][1]] = 1
    lab_copy[coord[1][0]][coord[1][1]] = 1
    lab_copy[coord[2][0]][coord[2][1]] = 1
    queue = deque([])
    #
    for i in range(len(viruses)):
        queue.append(viruses[i])
    #
    while queue:
        center = queue.popleft()

        for k in range(4):
            new_y = center[0] + dy[k]
            new_x = center[1] + dx[k]
            if 0 <= new_y < n and 0 <= new_x < m and lab_copy[new_y][new_x] == 0 and (not visited[new_y][new_x]):
                lab_copy[new_y][new_x] = 2
                queue.append([new_y, new_x])
                visited[new_y][new_x] = 1
    answer = max(answer, findSecure(lab_copy))
    lab_copy = copy.deepcopy(lab_og)

print(answer)
