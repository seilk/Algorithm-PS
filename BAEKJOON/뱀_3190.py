import sys
from collections import deque
sys.setrecursionlimit(10**5)
In = lambda : sys.stdin.readline().rstrip()
MIS = lambda : map(int, In().split())

def playGame(hx,hy ,tx,ty ,ap ,t ,chd,ctd,pre):
  visited[hx][hy]=1
  nhd = chd #해당 시간에 방향 변화 확인
  if time[t]!=0:
    nhd = dir[chd][dirIdx[time[t]]]
    pre.append([(hx,hy),time[t]])
  dhx,dhy=dir[nhd][0] #머리의 이후 진행 방향의 변화량
  nhx,nhy=hx+dhx,hy+dhy #머리의 새로운 좌표

  ntd=ctd #꼬리의 현재 방향
  if pre and (tx,ty)==pre[0][0]: #현재 꼬리의 위치가 이전에 머리가 회전한 방향
    arr=pre.popleft()
    ntd=dir[ctd][dirIdx[arr[1]]]
  dtx,dty=dir[ntd][0] #꼬리의 새로운 방향
  ntx,nty=tx+dtx,ty+dty #꼬리의 새로운 좌표

  visited[tx][ty]=0 #꼬리가 앞으로 나아가는 경우
  if board[hx][hy]==1:
    ap+=1
    board[hx][hy]=0
    ntx,nty=tx,ty
    visited[tx][ty]=1 #꼬리가 앞으로 나아가지 않는 경우
  if nhx<1 or N<nhx or nhy<1 or N<nhy: # 경계값 1
    return t+1
  if visited[nhx][nhy]==1:
    return t+1
  return playGame(nhx,nhy,ntx,nty,ap,t+1,nhd,ntd,pre)


if __name__=="__main__":
  N = int(In())
  K = int(In())
  board = [[0]*(N+1) for i in range(N+1)]
  for k in range(K):
    x,y=MIS()
    board[x][y]=1
  L = int(In())
  time = [0]*10001
  for l in range(L):
    t, d = In().split()
    time[int(t)]=d

  dirIdx={"L":1, "D":2}
  dir = [[(0,1),1,2],
         [(-1,0),3,0],
         [(1,0),0,3],
         [(0,-1),2,1]] #L,D

  visited=[[0]*(N+1) for i in range(N+1)]
  visited[1][1]=1
  print(playGame(1,2,1,1,0,1,0,0,deque([])))
  print()