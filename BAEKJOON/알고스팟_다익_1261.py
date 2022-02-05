import sys
from heapq import heappush, heappop
In = lambda : sys.stdin.readline().rstrip()
MIS = lambda : map(int, In().split())

def numberingMaze():
  cnt=0
  for i in range(R):
    for j in range(C):
      maze_num[i][j]=cnt
      cnt+=1


def daik():
  hq = []
  for n in range(R*C):
    heappush(hq, (0,n)) if n == 0 else heappush(hq, (INF,n))
  while hq:
    weight, a = heappop(hq)
    if dist[a] < weight:
      continue
    for ww, b in maze_two[a]:
      if dist[b] > dist[a] + ww:
        dist[b] = ww + weight
        heappush(hq,(dist[b], b))

if __name__ == "__main__":
  C,R=MIS()
  maze=[[*map(int, list(In()))] for i in range(R)]
  maze_num=[[0]*C for i in range(R)]
  numberingMaze()
  maze_two=[[] for i in range(R*C)]
  for r in range(R):
    for c in range(C):
      a=maze_num[r][c]
      for nr, nc in [(r-1, c), (r, c-1), (r+1,c), (r,c+1)]: # 4방향을 모두 확인해야함
        if 0<=nr<R and 0<=nc<C:
          b=maze_num[nr][nc]
          w = 1 if maze[nr][nc] == 1 else 0
          maze_two[a].append((w, b))
  INF = float("inf")
  dist = [INF for n in range(R*C)]
  dist[0]=0
  daik()
  print(dist[C*R-1])