import sys
from math import sqrt, pow
from heapq import heappush, heappop
In = lambda : sys.stdin.readline()
MIS = lambda : map(int, In().split())

def dcal(c1, c2):
  x1,y1 = c1
  x2,y2 = c2
  return sqrt(pow(abs((x1-x2)),2) + pow(abs((y1-y2)),2))

def mst(hq):
  ans=0
  while hq:
    dd, cc, cur = heappop(hq) #거리, 좌표, 현재 노드
    if not vist[cur]:
      ans+=dd
      vist[cur]=1
      for n in range(1,N+1): # 현재 노드를 제외한 다른 모든 노드에서 최단 거리 파악
        if n!=cur and not vist[n]:
          heappush(hq,(dcal(cc, coords[n]), coords[n], n))
  return ans


N,M=MIS()
coords = [-1]
for n in range(N):
  coords.append(tuple(MIS()))

vist = [0]*(N+1)
hq=[]
for m in range(M):
  f,t=MIS()
  vist[f], vist[t] = 1, 1
  for i in range(1,N+1):
    if not vist[i]:
      heappush(hq, (dcal(coords[f], coords[i]), coords[i], i))
      heappush(hq, (dcal(coords[t], coords[i]), coords[i], i))
print("{:.2f}".format(round(mst(hq),2)))
