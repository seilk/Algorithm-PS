import sys
In = lambda : sys.stdin.readline().rstrip()
MIS = lambda : map(int, In().split())
sys.setrecursionlimit(10**5)

def find(x):
  global cnt
  if tree[x]==x:
    return x
  tree[x]=find(tree[x])
  return tree[x]

def union(x,y):
  a=find(x)
  b=find(y)
  if a==b:
    return
  if a>b: tree[a]=b
  else: tree[b]=a

N,M=MIS()
tree=[i for i in range(N+1)]

cnt=0
# 처음부터 1을 루트노드로 생각하고 union을 해버리면 연결된 정보가 훼손되기 때문에
# 사이클을 찾기 매우 어려워진다.
# 하나씩 이어가면서 사이클을 먼저 찾는 방식으로 풀어야 한다.
for m in range(M):
  u,v=MIS()
  if find(u)!=find(v):
    union(u,v)
  else:
    cnt+=1

for m in range(1,N+1):
  if find(m)!=1:
    union(m,1)
    cnt+=1

print(cnt)