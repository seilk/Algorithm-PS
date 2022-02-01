import sys
sys.setrecursionlimit(10**4)
In = lambda : sys.stdin.readline().rstrip()
MIS = lambda : map(int, In().split())
def findMaxSum(r, c):
  global MXX, R, C
  if sum(sum(visited[i]) for i in range(R)) == R*C:
    MXX = max(MXX, sum(tmp))
    return
  for i in range(r,R):
    cc = c + 1 if i == r else 0
    for j in range(cc,C):
      flg = True
      for pi, pj in [(i-1,j), (i,j-1)]:
        if 0<=pi<R and 0<=pj<C:
          if not visited[pi][pj]:
            flg = False
            break
      if not visited[i][j] and flg:
        for ni, nj in [(i,j),(i+1,j),(i+2,j),(i+3,j)]:
          if 0<=ni<R and 0<=nj<C:
            flgg = True
            for ki in range(i,ni+1):
              if visited[ki][nj]:
                flgg = False
                break
            if flgg:
              for ii in range(i,ni+1):
                visited[ii][nj]=1
              tmp.append(int("".join([arr[iii][j] for iii in range(i,ni+1)])))
              findMaxSum(i, j)
              tmp.pop()
              for ii in range(i,ni+1):
                visited[ii][nj]=0
        for ni, nj in [(i,j+1),(i,j+2),(i,j+3)]:
          if 0<=ni<R and 0<=nj<C:
            flgg = True
            for kj in range(j,nj+1):
              if visited[ni][kj]:
                flgg = False
                break
            if flgg:
              for jj in range(j,nj+1):
                visited[ni][jj]=1
              tmp.append(int("".join([arr[i][jjj] for jjj in range(j,nj+1)])))
              findMaxSum(i, j)
              tmp.pop()
              for jj in range(j,nj+1):
                visited[ni][jj]=0

if __name__=="__main__":
  R, C = MIS()
  arr=[list(In()) for i in range(R)]
  visited = [[0]*C for i in range(R)]
  tmp = []
  MXX = -1
  findMaxSum(0,-1)
  print(MXX)