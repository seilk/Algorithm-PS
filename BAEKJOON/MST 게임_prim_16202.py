import sys
from heapq import heappush, heappop
In = lambda : sys.stdin.readline().rstrip()
MIS = lambda : map(int, In().split())

def prim():
  INF=float("inf")
  hq = [(0,1,1)] # 가중치, 출발노드, 도착노드
  vist = [0]*(1+N)
  ans=0
  minW=INF
  minE=(-1,-1)
  cnt=0
  while hq:
    w,a,b=heappop(hq)
    if not vist[b]:
      vist[b]=1
      ans+=w
      cnt+=1
      if minW > w and a!=b:
        minE = (a,b)
        minW = w
      for i in range(1,N+1):
        if grp[b][i]!=-1:
          if not vist[i]:
            heappush(hq, (grp[b][i], b, i))
  if cnt!=N:
    return False
  return ans,minE


N,M,K = MIS()

grp = [[-1]*(N+1) for i in range(N+1)]
for m in range(1,M+1):
  x,y=MIS()
  grp[x][y] = m
  grp[y][x] = m

ans=[]
for k in range(K):
  res=prim()
  if res==False:
    ans.append(0)
    break
  ans.append(res[0])
  grp[res[1][0]][res[1][1]] = -1
  grp[res[1][1]][res[1][0]] = -1

for i in range(K-1-k): ans.append(0)
print(*ans)