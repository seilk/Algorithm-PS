import sys
from math import sqrt, pow
In = lambda : sys.stdin.readline().rstrip()
MIS = lambda : map(int, In().split())

def dcal(a,b):
  x1, y1 = a
  x2, y2 = b
  return sqrt(pow(abs(x1-x2),2) + pow(abs(y1-y2),2))

def find(i):
  if grp[i]!=i:
    grp[i]=find(grp[i])
  return grp[i]

def union(x,y):
  a=find(x)
  b=find(y)
  if a!=b:
    grp[max(a,b)]=min(a,b)

def krus():
  ans=0
  for d,a,b in edges:
    if find(a)!=find(b):
      union(a,b)
      ans+=d
  return ans

N,M = MIS()
crd = []
edges = []
for c in range(N):
  crd.append((tuple(MIS())))
for m in range(M):
  a,b = MIS()
  edges.append((0,a-1,b-1))

for i in range(N):
  for j in range(i+1,N):
    edges.append((dcal(crd[i], crd[j]), i, j))

edges.sort(key=lambda x : x[0])

grp = [i for i in range(N)]
print("{:.2f}".format(round(krus(),2)))
