# https://ongveloper.tistory.com/376
import sys
from heapq import *
from math import sqrt

In = lambda : sys.stdin.readline()
MIS = lambda : map(int, In().split())

def dcal(c1, c2):
  x1,y1 = c1
  x2,y2 = c2
  return sqrt((abs(x1-x2)*abs(x1-x2) + abs(y1-y2)*abs(y1-y2)))

def mst():
  INF = float("inf")
  vist = [0]*(N+1)
  d=[]
  vist[0] = 1 # dummy
  vist[1] = 1 # 임의의 출발 노드 : 1번 노드
  ans=0 # 정답값 초기화

  # heapq 초기화 과정
  for i in range(1,N+1):
    # 임의의 출발 노드와 다른 노드 사이의 거리를 heappush
    heappush(d, (con[1][i], i))

  while d: #
    minE, minV = heappop(d)
    if not vist[minV]:
      ans+=minE
      vist[minV]=1
      for i in range(1,N+1):
        if not vist[i]:
          heappush(d,(con[minV][i],i))
  return ans


N,M=MIS()
INF = float("inf")
con=[[INF]*(N+1) for i in range(N+1)] # N*N 2차원 리스트, i와 j의 연결 가중치를 나타냄
crd=[()]
for n in range(N):
  crd.append(tuple(MIS()))

for i in range(1,N+1):
  for j in range(i+1,N+1):
    dres=dcal(crd[i],crd[j])
    con[i][j]=dres
    con[j][i]=dres

for m in range(M):
  f,t=MIS()
  con[f][t]=0
  con[t][f]=0

print(format(round(mst(),2),".2f"))
