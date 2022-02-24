import sys
from collections import deque
from heapq import heappush, heappop

In = lambda : sys.stdin.readline().rstrip()
MIS = lambda : map(int, In().split())

# 풀이 순서
# 1. 섬 번호 매기기
# 2. 섬에서 상하좌우 직선으로 이동해서 다른 섬 찾는 함수 만들기
# 3. 만약 A->B 섬의 최단경로가 갱신될 수 있으면 갱신 해주기
# 4. 최소 스패닝 트리로 모든 번호를 연결하는 가장 최단 경로 구하기(prim)

def numbering(num,x,y):
  dq=deque([(x,y)])
  visited[x][y]=1
  isl[x][y]=num
  while dq:
    r,c = dq.popleft()
    for nr, nc in [(r-1,c),(r+1,c),(r,c+1),(r,c-1)]:
      if 0<=nr<N and 0<=nc<M and not visited[nr][nc] and isl[nr][nc]>=1:
        visited[nr][nc]=1
        isl[nr][nc]=num
        dq.append((nr,nc))
  islnums.append(num)

def findEdge(x,y,num):
  for i in range(x+1,N): # 아래로 이동
    if isl[i][y]==num: # 현재 번호와 동일한 번호인 경우 break
      break
    elif isl[i][y]>=1:
      if i-x-1>1: # 다리의 길이가 1보다 큰 경우에만
        if grp[num][isl[i][y]]==0 or grp[num][isl[i][y]]>i-x-1:
          grp[num][isl[i][y]]=i-x-1
      break

  for i in range(x-1,-1,-1): # 위로 이동
    if isl[i][y]==num:
      break
    elif isl[i][y]>=1:
      if x-i-1>1:
        if grp[num][isl[i][y]]==0 or grp[num][isl[i][y]]>x-i-1:
          grp[num][isl[i][y]]=x-i-1
      break

  for i in range(y+1,M): # 오른쪽 이동
    if isl[x][i]==num:
      break
    elif isl[x][i]>=1:
      if i-y-1>1:
        if grp[num][isl[x][i]]==0 or grp[num][isl[x][i]]>i-y-1:
          grp[num][isl[x][i]]=i-y-1
      break

  for i in range(y-1,-1,-1): # 왼쪽 이동
    if isl[x][i]==num:
      break
    if isl[x][i]>=1:
      if y-i-1>1:
        if grp[num][isl[x][i]]==0 or grp[num][isl[x][i]]>y-i-1:
          grp[num][isl[x][i]]=y-i-1
      break

def mst(size): #최소스패닝 트리 알고리즘 - prim
  visited=[0]*(size)
  hq=[(0,1)]
  ans=0
  while hq:
    w,n=heappop(hq)
    if not visited[n]:
      ans+=w
      visited[n]=1
      for ww, nn in grpp[n]:
        if not visited[nn]:
          heappush(hq,(ww,nn))
  flg = sum(visited[1:])
  return ans if flg==size-1 else -1

N,M=MIS()
isl=[[*MIS()] for i in range(N)]
num=1 # 섬 번호
visited=[[0]*M for n in range(N)]

islnums=[] # 섬의 번호 (노드) 저장 [1,2,3,4]
for r in range(N):
  for c in range(M):
    if not visited[r][c] and isl[r][c]==1:
      numbering(num,r,c)
      num+=1

grp = [[0]*(islnums[-1]+1) for i in range(islnums[-1]+1)] #V*V # 인접리스트로 그래프 구현
for r in range(N):
  for c in range(M):
    if isl[r][c]>=1:
      findEdge(r,c,isl[r][c])

grpp=[[] for i in range(islnums[-1]+1)] #[[(w,nn),... ] [] [] []]
for i in range(1,islnums[-1]+1):
  for j in range(1,islnums[-1]+1):
    if grp[i][j]!=0:
      grpp[i].append((grp[i][j], j)) # weight, node
print(mst(islnums[-1]+1))