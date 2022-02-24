import sys
from heapq import heappop, heappush
def Mst():
  hq=[]
  cnt=1
  start=1
  tot=0
  selected[1] = 0
  for weight, end in grp[start]: # 1번 노드와 연결된 간선 hq에 전부 푸시
    if selected[end] < 0:
      heappush(hq, (weight,end))
  while cnt < V:
    weight,end = heappop(hq)
    if selected[end]<0:
      cnt+=1
      tot+=weight # 전체 가중치 누적합
      selected[end]=weight # 최소 가중치가 몇인지 기록함
      for weight, node in grp[end]: # 뽑힌 end와 연결된 간선 푸시
        if selected[node]<0:
          heappush(hq, (weight,node))
  return tot

if __name__ == "__main__":
  In = lambda : sys.stdin.readline().rstrip()
  MIS = lambda : map(int, In().split())
  V, E = MIS()
  grp = [[]for i in range(V + 1)]
  selected = [-1 for i in range(V + 1)]
  for _ in range(E):
    start,end,weight=MIS()
    grp[start].append((weight,end))
    grp[end].append((weight,start))
  tot = Mst()
  print(tot - max(selected[1:]))
