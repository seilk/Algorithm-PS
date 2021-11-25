# ----------Title
# 아기상어
# Gold IV
# https://boj.kr/16236

# ----------Tip
# 구현
# 구현력 키우는데 정말 도움!!
# 구현 문제에서는 조건을 Notetaking 하면서 풀 것
# 무한 loop를 막는 Condition을 물고기의 Total로 풀면 안됐었음

# ----------URLs

# ----------Code with Detail
import sys
from collections import deque
sys.setrecursionlimit(10 ** 9)
def input(): return sys.stdin.readline().rstrip()


g = int(input())
ocean = [list(map(int, input().split())) for i in range(g)]
sksize = 2
tot = 0
for i in range(g):
  for j in range(g):
    k = ocean[i][j]
    if 0 < k < 7:
      tot += 1
    if k == 9:
      shark = (i, j)

ans = 0  # 정답 시간
cnt = 0  # 먹은 물고기 수
while 1:  # 물고기가 존재할 때만 반복
  queue = deque([(shark[0], shark[1])])  # 상어의 좌표
  visited = [[-1] * g for i in range(g)]  # visited 초기화
  check = [[0] * g for i in range(g)]
  check[shark[0]][shark[1]] = 1
  res = 999  # 시간 단축1
  while queue:
    r, c = queue.popleft()
    for nr, nc in ([(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]):  # 4방향 탐색
      # grid 범위 내, 방문안한 곳
      if 0 <= nr < g and 0 <= nc < g and not(check[nr][nc]):
        if (ocean[nr][nc] <= sksize):  # 상어의 크키보다 작거나 같은 경우
          if (ocean[nr][nc] < sksize and ocean[nr][nc] != 0):  # 상어의 크기보다 작은 경우 but not 0
            visited[nr][nc] = visited[r][c] + 1  # 출발칸 + 1
            if visited[nr][nc] == res:
              if sr == nr:  # 높이가 같을 때
                if nc < sc:  # nc가 sc보다 더 왼쪽에 있을 때
                  sr = nr
                  sc = nc
              elif sr > nr:  # 높이가 다를 때
                sr = nr
                sc = nc
            elif visited[nr][nc] < res:
              res = visited[nr][nc]  # res 갱신
              sr = nr
              sc = nc
          else:
            visited[nr][nc] = visited[r][c] + 1
            queue.append((nr, nc))
        check[nr][nc] = 1

  if res == 999:  # res가 갱신이 안된 경우
    break
  time = res + 1
  ans += time
  cnt += 1
  tot -= 1
  if cnt == sksize:
    sksize += 1
    cnt = 0
  ocean[shark[0]][shark[1]] = 0
  shark = (sr, sc)
  ocean[shark[0]][shark[1]] = 9
print(ans)
# 3
# 0 0 0
# 0 0 3
# 9 3 1
# 20
# 1 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
# 6 6 6 6 6 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
# 1 2 6 2 9 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
# 2 2 6 2 6 6 2 2 2 2 2 2 2 2 2 2 2 2 2 2
# 6 2 2 2 6 6 2 2 2 2 2 2 2 2 2 2 2 2 2 2
# 6 6 6 6 6 6 2 2 2 2 2 2 2 2 2 2 2 2 2 2
# 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
# 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
# 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
# 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
# 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
# 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
# 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
# 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
# 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
# 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
# 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
# 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
# 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
# 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2

# 10
# 2 3 4 0 0 0 3 4 0 1
# 0 3 0 4 6 2 4 1 0 5
# 0 5 0 4 3 1 1 1 1 0
# 3 5 6 1 4 5 5 2 4 6
# 1 3 4 0 5 4 0 0 2 0
# 0 0 6 0 4 4 3 1 0 5
# 1 6 0 1 3 0 3 0 6 4
# 0 0 1 4 5 1 3 2 0 6
# 6 0 5 6 1 1 9 6 0 0
# 0 4 5 3 6 5 2 1 0 1

# 6
# 1 0 0 0 0 0
# 6 6 6 6 6 0
# 1 0 6 0 9 0
# 2 0 6 0 6 6
# 6 0 0 0 6 6
# 6 6 6 6 6 6

# 3
# 0 1 1
# 5 5 5
# 0 9 0

# 2
# 9 3
# 3 1
