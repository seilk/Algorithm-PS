import sys
from collections import deque
sys.setrecursionlimit(10**5)

def ROTATE(plate):
  new_plate = [[0]*5 for i in range(5)]
  for i in range(5):
    for j in range(5):
      if plate[i][j] == 1:
        new_plate[j][4-i] = 1
  return new_plate

def BFS(MAZE):
  dq = deque([(0,0,0)])
  visitedcube = [[[-1]*5 for i in range(5)] for j in range(5)]
  visitedcube[0][0][0] = 0
  while dq:
    x,y,z = dq.popleft()
    for nx,ny,nz in [(x+1,y,z),(x-1,y,z),(x,y+1,z),(x,y-1,z),(x,y,z-1),(x,y,z+1)]:
      if 0<=nx<5 and 0<=ny<5 and 0<=nz<5:
        if visitedcube[nx][ny][nz] < 0 and MAZE[nx][ny][nz] == 1:
          visitedcube[nx][ny][nz] = visitedcube[x][y][z] + 1
          if nx==4 and ny==4 and nz==4:
            return visitedcube[4][4][4]
          dq.append((nx,ny,nz))
  return 1e9 if visitedcube[4][4][4]==-1 else visitedcube[4][4][4]

def DFS(depth):
  global mnn
  if depth == 5: # 미로가 전부 완성되면 한번 BFS 시도함
    if MAZE[0][0][0] == 1:
      mnn = min(BFS(MAZE), mnn)
    return
  for i in range(5):
    if not visitedplate[i]:
      visitedplate[i] = 1
      for r in range(4): #4번 회전 (원본 포함)
        new_plate = ROTATE(MAPP[i])
        MAPP[i] = new_plate
        MAZE.append(new_plate)
        DFS(depth+1)
        MAZE.pop()
      visitedplate[i] = 0



In = lambda : sys.stdin.readline().rstrip()
MIS = lambda : map(int, In().split())
MAPP = [[list(MIS()) for i in range(5)] for j in range(5)]
visitedplate = [0]*5
MAZE = []
mnn = 1e9
DFS(0)
print(-1) if mnn == 1e9 else print(mnn)
