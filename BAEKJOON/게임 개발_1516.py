import sys
from heapq import heappush, heappop


In = lambda : sys.stdin.readline().rstrip()
MIS = lambda : map(int, In().split())


def topo():
  hq=[]
  for i in range(1,N+1):
    if indeg[i]==0:
      ans[i]=prc[i]
      heappush(hq,(prc[i],i))

  while hq:
    p, nd = heappop(hq)
    for pp,x in fromto[nd]:
      indeg[x]-=1
      if indeg[x]==0 and not ans[x]:
        ans[x]=p+pp
        heappush(hq,(p+pp, x))

N = int(In())
indeg=[0]*(1+N)
fromto=[[] for i in range(N+1)]
prc=[0]*(N+1)
ans=[0]*(N+1)
for i in range(1, N+1):
  info=[*MIS()]
  prc[i]=info[0]
  for j in range(1,len(info)-1):
    fromto[info[j]].append((prc[i],i))
    indeg[i]+=1
topo()
print(*ans[1:], sep="\n")
