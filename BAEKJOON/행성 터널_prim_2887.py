import sys
from heapq import heappush, heappop
In = lambda : sys.stdin.readline().rstrip()
MIS = lambda : map(int, In().split())

def find(x):
  if grp[x]!=x:
    grp[x]=find(grp[x])
  return grp[x]

def union(x,y):
  a=find(x)
  b=find(y)
  if a!=b:
    grp[max(a,b)]=min(a,b)

def krusk():
  vist = [0]*N
  tot=0
  tmp=[]
  for n in range(N):
    if not vist[n]:
      ww=float("inf")
      wn=-1
      for m in range(n+1,N):
        tw = min(abs(X[m]-X[n]),abs(Y[m]-Y[n]),abs(Z[m]-Z[n]))
        if ww>tw:
          ww=tw
          wn=m
      tot+=ww
      vist[n],vist[wn]=1,1

  return tot

N = int(In())
X,Y,Z = [],[],[]
for n in range(N):
  x,y,z=MIS()
  X.append(x)
  Y.append(y)
  Z.append(z)

grp = [i for i in range(N)]
print(prim())