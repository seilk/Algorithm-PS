import sys
from collections import deque
In = lambda : sys.stdin.readline().rstrip()
MIS = lambda : map(int, In().split())

def search(r,c):
  res=[]
  for nr, nc in [(r+1,c+1),(r+1,c),(r,c+1)]:
    if dpv[nr][nc]==0:
      return False
    res.append(dpv[nr][nc])
  return res

n,m=MIS()
arr=[[*map(int, list(In()))]+[0] for i in range(n)]+[[0]*(m+1)]
dpv=[[0]*(m+1) for i in range(n+1)]
maxx=0
for r in range(n-1,-1,-1):
  for c in range(m-1,-1,-1):
    if arr[r][c]==1:
      res=search(r,c)
      if res:
        if dpv[r+1][c+1]==dpv[r+1][c]==dpv[r][c+1]:
          dpv[r][c]=dpv[r+1][c+1]+1
        else:
          dpv[r][c] = min(res)+1
      else: dpv[r][c]=1
      maxx= max(dpv[r][c],maxx)
print(maxx**2)

# 3 4
# 1111
# 1110
# 1111