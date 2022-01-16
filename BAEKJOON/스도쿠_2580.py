import sys
from collections import defaultdict


def init(a):
  for i in range(9):
    for j in range(9):
      if sdoku[i][j] == 0:
        emptycoords.append((i, j))
      a = makeBoxGroup(i, j)
      boxgroup[a].append((i, j))
      boxgroupcheck[i][j] = a
      if sdoku[i][j] > 0:
        boxgroup_num[a][sdoku[i][j]] = 1
        rowgroup_num[i][sdoku[i][j]] = 1
        colgroup_num[j][sdoku[i][j]] = 1


def makeBoxGroup(i, j):
  if 0 <= i < 3:
    if 0 <= j < 3:
      a = 0
    elif 3 <= j < 6:
      a = 1
    else:
      a = 2
  elif 3 <= i < 6:
    if 0 <= j < 3:
      a = 3
    elif 3 <= j < 6:
      a = 4
    else:
      a = 5
  else:
    if 0 <= j < 3:
      a = 6
    elif 3 <= j < 6:
      a = 7
    else:
      a = 8
  return a


def findNum(depth):
  global complete
  if depth == len(emptycoords):
    for i in range(9):
      print(*sdoku[i])
    sys.exit(0)
    return
  for i in range(len(emptycoords)):
    if not visited[i]:
      x, y = emptycoords[i]
      key = str(x) + str(y)
      b = boxgroupcheck[x][y]
      for num in emptycoords_can[key]:
        if boxgroup_num[b][num] == 0 and rowgroup_num[x][num] == 0 and colgroup_num[y][num] == 0:
          visited[i] = 1
          sdoku[x][y] = num
          boxgroup_num[b][num], rowgroup_num[x][num], colgroup_num[y][num] = 1, 1, 1
          findNum(depth + 1)
          sdoku[x][y] = 0
          boxgroup_num[b][num], rowgroup_num[x][num], colgroup_num[y][num] = 0, 0, 0
          visited[i] = 0
      if sdoku[x][y] == 0:
        return


def checkCanNum():
  global a
  for x, y in emptycoords:
    visited = [0] * 10
    a = boxgroupcheck[x][y]
    for i, j in boxgroup[a]:  # 3 * 3 그룹
      visited[sdoku[i][j]] = 1
    for rv in sdoku[x]:  # row 그룹
      visited[rv] = 1
    for c in range(9):  # col 그룹
      visited[sdoku[c][y]] = 1
    key = str(x) + str(y)  # 00 ~ 88
    for v in range(1, 10):
      if visited[v] == 0:
        emptycoords_can[key].append(v)


input = sys.stdin.readline
sdoku = [[*map(int, input().split())] for i in range(9)]
emptycoords = []
emptycoords_can = defaultdict(list)
rowgroup_num = [[0] * 10 for i in range(9)]
colgroup_num = [[0] * 10 for i in range(9)]
boxgroup_num = [[0] * 10 for i in range(9)]
boxgroup = [[] for i in range(9)]
boxgroupcheck = [[0] * 9 for i in range(9)]
init(0)
checkCanNum()
visited = [0 for i in range(len(emptycoords))]
complete = False
findNum(0)
