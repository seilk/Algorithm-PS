import sys
In = lambda : sys.stdin.readline().rstrip()
MIS = lambda : map(int, In().split())
sys.setrecursionlimit(10**6)

def f(p,w,d):
  global mxx
  if mxx[1]<w:
    mxx=(p,w)
  for c, ww in tree[p]:
    if not visited[c]:
      visited[c]=1
      f(c,w+ww,d+1)
      visited[c]=0

N=int(In())
tree=[[] for i in range(N+1)]
for _ in range(N-1): #트리의 간선은 N-1개
  p,c,w=MIS()
  tree[p].append((c,w))
  tree[c].append((p,w))

visited=[0]*(1+N)
visited[1]=1
mxx=(1,0)
f(1,0,0)
d1=mxx[0]
mxx=(1,0)
visited[1],visited[d1]=0,1
f(d1,0,0)
print(mxx[1])