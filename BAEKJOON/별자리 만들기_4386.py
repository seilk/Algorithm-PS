import sys
from heapq import heappop, heappush


def calDistance(x1,y1,x2,y2):
  return (abs(x1-x2)**2+abs(y1-y2)**2)**(0.5)


def Mst():
  hq = []
  for d, end in grp[0]:
    heappush(hq,(d,end))
  selected[0]=0
  cnt = 1
  tot = 0
  while cnt < n:
    d, end = heappop(hq)
    if selected[end]<0:
      selected[end] = d
      tot+=d
      cnt+=1
      for d, node in grp[end]:
        if selected[node]<0:
          heappush(hq,(d,node))
  return tot


In = lambda : sys.stdin.readline().rstrip()
MIS = lambda : map(float, In().split())
n = int(In())
grp = [[] for i in range(n)]
stars = [tuple(MIS()) for v in range(n)]
for i in range(n):
  x1,y1 = stars[i]
  for j in range(i + 1, n):
    x2,y2 = stars[j]
    d=calDistance(x1,y1,x2,y2)
    grp[i].append((d,j))
    grp[j].append((d,i))
selected = [-1] * n
print("{:.2f}".format(Mst()))
