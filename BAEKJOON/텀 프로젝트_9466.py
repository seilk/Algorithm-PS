import sys
sys.setrecursionlimit(10**6)
In = lambda : sys.stdin.readline().rstrip()
MIS = lambda : map(int, In().split())

def findTeam(node, N):
  global included, arr, visited, endd, SUM
  visited[node]=1
  if included[arr[node]]!=0: # 어떤 그룹에 이미 포함되어 있거나 그룹을 이루지 못한 경우
    visited[node]=0
    included[node]=-1
    return False
  if arr[node] == node: # 자기자신
    included[node]=1
    SUM+=1
    return False
  if visited[arr[node]]: # 현재 노드가 가리키는 노드가 이미 중간에 선택된 노드라면
    included[node]=1
    SUM+=1
    endd = arr[node]
    return True
  if findTeam(arr[node], N):
    visited[node] = 0
    if node == endd:
      SUM+=1
      included[node] = 1
      return False
    included[node] = 1
    SUM+=1
    return True
  visited[node]=0
  included[node]=-1
  return False

def solve():
  global arr, included, visited, endd, SUM
  N=int(In())
  arr=[-1]+[*MIS()]
  included=[0]*(N+1)
  visited=[0]*(N+1)
  SUM=0
  for node in range(1, N+1):
    if not included[node]:
      endd = 0
      findTeam(node,N)
  print(N-SUM)

if __name__ == "__main__":
  T = int(In())
  for t in range(T):
    solve()
