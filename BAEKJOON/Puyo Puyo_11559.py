# ----------Title
# Puyo Puyo
# Gold IV
# https://boj.kr/11559
# ----------Tip
# BFS
# 구현
# ----------URLs

# ----------Code with Detail
import sys
from collections import deque


def pang(x, y, clr):  # BFS
  cnt = []
  queue = deque([(x, y)])
  visited = [[0] * 6 for i in range(12)]
  while queue:
    x, y = queue.popleft()
    for nx, ny in [(x - 1, y), (x + 1, y), (x, y + 1), (x, y - 1)]:
      if (0 <= nx < 12) and (0 <= ny < 6):
        if not visited[nx][ny]:
          if fld[nx][ny] == clr:
            visited[nx][ny] = 1
            queue.append((nx, ny))
            cnt.append((nx, ny))
  if len(cnt) >= 4:  # 뿌요 터지면서 빈 공간으로 갱신
    for x, y in cnt:
      fld[x][y] = "."
    return True


def swap(clr, x, y):  # 뿌요 교환
  fld[x][y] = clr
  fld[x - 1][y] = "."


def fall():  # 수직으로만 떨어짐
  for i in range(11, -1, -1):
    for j in range(6):
      if fld[i][j] != ".":
        tmp = i + 1
        clr = fld[i][j]
        while (tmp < 12) and fld[tmp][j] == ".":
          swap(clr, tmp, j)
          tmp += 1


if __name__ == "__main__":
  input = sys.stdin.readline
  fld = [list(input().rstrip()) for i in range(12)]
  chain = 0
  while 1:
    flg = False
    for i in range(11, -1, -1):
      for j in range(6):
        if fld[i][j] != ".":
          clr = fld[i][j]
          if pang(i, j, clr):
            flg = True
    if flg:
      chain += 1
      fall()
      continue
    else:
      break
  print(chain)
