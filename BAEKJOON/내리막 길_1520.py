# ----------Title
# 내리막 길
# Gold IV
# https://boj.kr/1520

# ----------Tip
# DFS + Memoization

# ----------URLs

# ----------Code with Detail
import sys
sys.setrecursionlimit(10 ** 9)
def input(): return sys.stdin.readline().rstrip()


def DFS(row, col, pre):
  # 제한사항 : row와 col의 range, 방문여부, 이전 값보다 작은 값
  if 0 <= row < rowsize and 0 <= col < colsize and not visited[row][col] and mapp[row][col] < pre:
    #조건을 만족하는 좌표에서 cache값이 존재하면 그대로 가져다 쓴다. ##DP MEMOIZATION##
    if cache[row][col] != -1:
      return cache[row][col]
    # 방문처리 및, cache값 처리 (0 -> 1)
    visited[row][col] = 1
    # cache[row][col] += 1

    # 4방향을 DFS로 탐색해 4방향 각각의 위치에서 가능한 경로 개수를 모두 더해줌
    cache[row][col] \
        = DFS(row + 1, col, mapp[row][col])\
        + DFS(row - 1, col, mapp[row][col])\
        + DFS(row, col + 1, mapp[row][col])\
        + DFS(row, col - 1, mapp[row][col])
    visited[row][col] = 0
    # for i in range(rowsize):
    #   print(*visited[i])
    # print("----")
    for i in range(rowsize):
      print(*cache[i])
    print()
  else:
    return 0
  # cache계산을 다 마치고 종료되는 함수에서는 cache값을 return 한다.
  return cache[row][col]


rowsize, colsize = map(int, input().split())
mapp = [list(map(int, input().split())) for i in range(rowsize)]
# -1로 초기화
cache = [[-1] * colsize for i in range(rowsize)]
cache[-1][-1] = 1
visited = [[0] * colsize for i in range(rowsize)]
DFS(0, 0, 10001)
print(cache[0][0])

# ----------TC
# 4 5
# 50 45 37 32 30
# 35 50 40 20 25
# 30 30 25 17 28
# 27 24 22 15 10

# 3 3
# 9 4 3
# 8 5 2
# 7 6 1

# 4 4
# 16 9 8 1
# 15 10 7 2
# 14 11 6 3
# 13 12 5 4
