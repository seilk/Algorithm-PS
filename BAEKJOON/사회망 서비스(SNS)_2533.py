import sys
In = lambda : sys.stdin.readline().rstrip()
MIS = lambda : map(int, In().split())
sys.setrecursionlimit(10**6)

def f(x):
  dp[x][1]=1
  visited[x]=1
  for z in tree[x] :
    if not visited[z]:
      f(z)
      dp[x][0]+=dp[z][1] # 현재 노드가 얼리어답터가 아니려면 주변노드(자식노드X)가 모두 얼리어답터여야한다.
      dp[x][1]+=min(dp[z]) # 현재 노드가 얼리어답터면 주변노드(자식노드X)의 최소값을 더해야한다.

N=int(In())
tree=[[] for i in range(N+1)]
dp=[[0,0] for i in range(N+1)]
for i in range(N-1):
  p,c=MIS()
  tree[p].append(c)
  tree[c].append(p)
visited=[0]*(1+N)
f(1)
print(min(dp[1]))