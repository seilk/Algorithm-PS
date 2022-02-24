import sys
def DFS(depth,r,c):
  global mxx
  if depth == R*C+1:
    mxx = max(depth, mxx)
    return
  mxx = max(depth, mxx)
  for nr, nc in [(r+1,c),(r,c+1),(r-1,c),(r,c-1)]:
    if 1<=nr<=R and 1<=nc<=C and not visited[ord(BOARD[nr][nc])-65]:
      idx = ord(BOARD[nr][nc])-65
      visited[idx] = 1
      DFS(depth+1,nr,nc)
      visited[idx] = 0

if __name__ == "__main__":
  In = lambda : sys.stdin.readline().rstrip()
  MIS = lambda : map(int, In().split())
  R, C = MIS()
  BOARD = [["."] * (R + 1)] + [["."] + list(In()) for i in range(R)]
  visited = [0] * 27
  visited[ord(BOARD[1][1])-65] = 1
  mxx = -1
  DFS(1,1,1)
  print(mxx)
