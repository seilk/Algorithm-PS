# ----------Title
# N-Queen
# Gold V
# https://www.acmicpc.net/problem/9663

# ----------Tip
# BackTracking
# 1차원 visited가 의미하는 것 ~ index는 체스판의 row ~ visited[index]는 체스판의 column
# 가로 세로에 한 개의 queen만 존재할 수 있음

# ----------URLs
#

# ----------Code with Detail
import sys
from collections import defaultdict
sys.setrecursionlimit(10**4)


def DFS(depth):
  global cnt
  if depth == n + 1:  # DFS 재귀탐색 완료 조건
    cnt += 1
    return
  for i in range(1, n + 1):
    if depth == 1:
      visited[depth] = i
      checkrow[i] = 1
      DFS(depth + 1)
      visited[depth] = 0
      checkrow[i] = 0
    elif not checkrow[i]:  # 같은 열이면 안됨
      flg = True
      for j in range(1, n + 1):  # row
        if visited[j] != 0:
          if (abs(depth - j) == abs(i - visited[j])):  # 대각선 위치 조건 파악
            flg = False  # 대각선에 위치하면 flg = False
            break
      if flg:
        visited[depth] = i
        checkrow[i] = 1
        DFS(depth + 1)
        visited[depth] = 0
        checkrow[i] = 0


if __name__ == "__main__":
  input = sys.stdin.readline
  n = int(input().rstrip())
  tmp = [i for i in range(1, n + 1)]
  visited = [0 for i in range(n + 1)]
  checkrow = [0 for i in range(n + 1)]
  cnt = 0
  DFS(1)
  print(cnt)
