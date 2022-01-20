import sys


def init(a):
  for i in range(9):
    for j in range(9):
      if sdoku[i][j] == 0:
        emptycoords.append((i, j))
      a = makeBoxGroup(i, j)
      if sdoku[i][j] > 0:
        boxgroup_num[a][sdoku[i][j]] = 1
        rowgroup_num[i][sdoku[i][j]] = 1
        colgroup_num[j][sdoku[i][j]] = 1


def makeBoxGroup(i, j):
  rb = i // 3
  cb = j // 3
  if rb == 0:
    return cb
  elif rb == 1:
    return cb + 3
  elif rb == 2:
    return cb + 6


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
      b = makeBoxGroup(x, y)
      for num in range(1,10):
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


input = sys.stdin.readline
sdoku = [[*map(int, input().split())] for i in range(9)]
emptycoords = []
rowgroup_num = [[0] * 10 for i in range(9)]  # O(1)
colgroup_num = [[0] * 10 for i in range(9)]
boxgroup_num = [[0] * 10 for i in range(9)]
init(0)
visited = [0 for i in range(len(emptycoords))]
complete = False
findNum(0)
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0
