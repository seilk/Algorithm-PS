# ----------Title
# 토마토
# Silver I
# https://www.acmicpc.net/problem/7576

# ----------Tip
# BFS
# 구현은 문제를 꼼꼼히 읽자

# ----------URLs


# ----------Code with Detail
import sys
from collections import deque
import heapq


def BFS(queue):
  while queue:
    t = len(queue)
    for i in range(t):
      r, c = queue.popleft()
      for nr, nc in [(r + 1, c), (r - 1, c), (r, c - 1), (r, c + 1)]:
        if 0 <= nr < rs and 0 <= nc < cs:
          if not visited[nr][nc]:
            visited[nr][nc] = visited[r][c] - 1  # visited에 날짜 mark
            queue.append((nr, nc))


if __name__ == "__main__":
  # Setting
  input = sys.stdin.readline
  cs, rs = map(int, input().split())
  queue = deque([])
  farm = []
  visited = [[0] * cs for i in range(rs)]
  flg = False
  for r in range(rs):
    tmp = list(map(int, input().split()))
    for c in range(cs):
      if tmp[c] == 1:
        visited[r][c] = -1
        queue.append((r, c))
      if tmp[c] == 0:
        flg = True
      if tmp[c] == -1:
        visited[r][c] = 1
    farm.append(tmp)

  if flg:  # 익을 수 있는 토마토가 있을 때
    BFS(queue)
    ans = 0
    for i in range(rs):
      if visited[i].count(0) > 0:
        ans = -1
        break
      heapq.heapify(visited[i])
      ans = max(ans, -heapq.heappop(visited[i]) - 1)
    print(ans)
  else:  # 토마토가 이미 모든 칸에서 익어있을 때
    print(0)


# 3 3
# 1 -1 1
# -1 1 -1
# 1 -1 1
