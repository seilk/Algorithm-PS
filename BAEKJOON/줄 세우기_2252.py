import sys
from collections import deque

In = lambda : sys.stdin.readline().rstrip()
MIS = lambda : map(int, In().split())

def topo():
  dq=deque([])
  for i in range(1,N+1):
    if indeg[i]==0:
      ans.append(i)
      dq.append(i)

  while dq:
    nd=dq.popleft()
    for nn in grp[nd]:
      indeg[nn]-=1
      if indeg[nn]==0 and not vist[nn]:
        vist[nn]=1
        ans.append(nn)
        dq.append(nn)

N,M=MIS()
indeg=[0]*(N+1)
grp=[[] for i in range(N+1)]
vist=[0]*(N+1)
ans=[]
for m in range(M):
  f,t=MIS()
  grp[f].append(t)
  indeg[t]+=1

topo()
print(*ans)
