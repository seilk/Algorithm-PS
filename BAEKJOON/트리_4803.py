import sys
In = lambda : sys.stdin.readline().rstrip()
MIS = lambda : map(int, In().split())
sys.setrecursionlimit(10**6)
def union(x,y):
  a=find(x)
  b=find(y)
  if a==b:
    return
  if a<b:grp[b]=a
  else:grp[a]=b

def find(x): # 부모노드를 찾아주는 함수
  if grp[x]==False: # 트리가 형성되지 않는 경우
    return False
  if grp[x]==x:
    return x
  grp[x] = find(grp[x])
  return grp[x]

tc=1
while 1:
  try:
    N,M=MIS()
    if N==0 and M==0:raise Exception
    grp=[i for i in range(N+1)]
    for _ in range(M):
      a,b=MIS()
      if find(min(a,b)) == find(max(a,b)):
        grp[min(a,b)]=False
      union(a,b)

    visited=[0]*(N+1)
    for n in range(1,N+1):
      x=find(n)
      if x and not visited[x]:
        visited[x]=1
    ans=sum(visited)
    if ans==1:
      print("Case {0}: There is one tree.".format(tc))
    elif ans>1:
      print("Case {0}: A forest of {1} trees.".format(tc, ans))
    else:
      print("Case {0}: No trees.".format(tc))
    tc+=1
  except:
    break

