import sys
# 최대 N*M의 연산을 하는 선형 LCA
sys.setrecursionlimit(10**5)
In = lambda : sys.stdin.readline().rstrip()
MIS = lambda : map(int, In().split())

def swap(a,b): # 기본적인 swap
  return b,a

def findDepth(x, p): # 깊이를 기록하는 함수, 부모노드는 for문 탐색에서 제외한다.
  depth[x]=depth[p]+1
  parent[x]=p
  for nx in tree[x]:
    if nx!=p:
      findDepth(nx, x)

def findLCA(x,y): # 깊이가 같은지 판단하고 다르다면 깊이를 맞추고 선형적으로 LCA를 찾아주는 함수
  if depth[x] < depth[y]: # 깊이가 더 깊은 변수를 x에 둔다.
    x,y=swap(x,y)
  while depth[x]!=depth[y]:
    x=parent[x]
  while x!=y:
    x=parent[x]
    y=parent[y]
  return x

N = int(In())
parent=[0]*(N+1)
tree=[[] for i in range(N+1)]
depth=[0]*(N+1) # 깊이 기록
for i in range(N-1): # 무조건 번호가 작은 노드가 부모노드라고 생각하고 풀면 안된다. (자주 하는 실수)
  a,b=MIS()
  tree[a].append(b)
  tree[b].append(a)

findDepth(1, 0)
M = int(In())
for m in range(M):
  x,y = MIS()
  if x == 1 or y == 1: # 두 노드중 하나라도 1이면 공통조상은 1임
    print(1)
    continue
  print(findLCA(x,y))
