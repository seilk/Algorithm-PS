import sys
from collections import deque
In = lambda : sys.stdin.readline().rstrip()
MIS = lambda : map(int, In().split())

def findRoute(R,C,MIRO):
  visited = [[[0,10001] for j in range(C+1)] for i in range(R+1)]
  dq = deque([(1,1)])
  visited[1][1][0] = 1
  visited[1][1][1] = 0
  while dq:
    r,c=dq.popleft()
    for nr, nc in [(r-1, c),(r,c-1),(r+1,c),(r,c+1)]:
      if 1<=nr<=R and 1<=nc<=C:
        if not visited[nr][nc][0]:
          visited[nr][nc][0] = visited[r][c][0]+1
          visited[nr][nc][1] = visited[r][c][1] if MIRO[nr][nc] == 0 else visited[r][c][1] + 1
          dq.append((nr,nc))
        elif MIRO[nr][nc] == 0 and visited[nr][nc][1] > visited[r][c][1]:
            visited[nr][nc][0] = visited[r][c][0]+1
            visited[nr][nc][1] = visited[r][c][1]
            dq.append((nr,nc))
        elif MIRO[nr][nc] == 1 and visited[nr][nc][1] > visited[r][c][1]+1:
            visited[nr][nc][0] = visited[r][c][0]+1
            visited[nr][nc][1] = visited[r][c][1]+1
            dq.append((nr,nc))
  return visited[R][C][1]

if __name__ == "__main__":
  C, R = MIS()
  MIRO = [[0]*(C+1)]+[[0]+[*map(int, list(In()))] for i in range(R)]
  ans=findRoute(R,C,MIRO)
  print(ans)

