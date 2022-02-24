import sys
from collections import deque
In = lambda : sys.stdin.readline().rstrip()
MIS = lambda : map(int, In().split())

def find(x,p):
  if p[x]!=x:
    p[x]=find(p[x],p)
  return p[x]

def union(x,y,p):
  a=find(x,p)
  b=find(y,p)
  if a!=b:
    p[max(a,b)]=min(a,b)

def krus(M,idx):
  ans=0
  mw=10001

  p = [i for i in range(N+1)]
  for e in range(M):
    w,x,y=edges[e] # 가중치, 노드1, 노드2
    if w != -1:
      if find(x,p)!=find(y,p): # 노드1과 노드2가 연결될 수 있는지 확인
        union(x,y,p) # 연결될 수 있으면 서로를 union
        ans+=w # 최소 스패닝 트리 가중치 합 계산

  f = find(1,p)
  for i in range(1,N+1):
    if find(i,p)!=f: # 모두 연결되어 있으면 모든 정점에서의 find()가 같아야함.
      return -1
  return ans

N,M,K = MIS()
edges = []

ans=[]
for m in range(1,M+1):
  x,y=MIS()
  edges.append([m, x, y])

edges.sort()
edges = deque(edges)
idx=0
for k in range(1,K+1):
  res = krus(M,idx)
  if res <= 0:
    ans.append(0)
    break
  edges.popleft()
  ans.append(res)
  M-=1

for i in range(k+1,K+1) : ans.append(0) # 0을 넣어주는 개수 주의
print(*ans)
