import sys
sys.setrecursionlimit(10**5)
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
  ans=0
  for w,a,b in edges:
    if find(a)!=find(b):
      union(a,b)
      ans+=w
  return ans

N = int(In())
X,Y,Z=[],[],[]
for n in range(N):
  x,y,z=MIS()
  X.append((x,n))
  Y.append((y,n))
  Z.append((z,n))

edges=[]
X.sort()
Y.sort()
Z.sort()
for i in range(1,N):
  edges.append((X[i][0]-X[i-1][0], X[i-1][1], X[i][1]))
  edges.append((Y[i][0]-Y[i-1][0], Y[i-1][1], Y[i][1]))
  edges.append((Z[i][0]-Z[i-1][0], Z[i-1][1], Z[i][1]))
edges.sort()
grp=[i for i in range(N)]
print(krusk())


