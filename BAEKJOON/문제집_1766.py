import sys
from heapq import heappop, heappush
In = lambda : sys.stdin.readline().rstrip()
MIS = lambda : map(int, In().split())
N, M = MIS()
pset = [] # 우선순위 큐
visited = [0]*(N+1) # 방문 여부 저장
ans=[] # 정답 저장
INDEG = [0]*(N+1) # Indegree 저장
OUT = [[] for i in range(N + 1)] # Outnodes 저장
for m in range(M):
  a, b = MIS()
  INDEG[b] += 1
  OUT[a].append(b)
for i in range(1, N + 1):
  heappush(pset, [INDEG[i], i, OUT[i]])
while pset:
  ind, cur, out_nodes = heappop(pset) # indegree = 0 인 node 삭제
  if ind == 0:
    if not visited[cur]:
      visited[cur] = 1
      for n in out_nodes:
        if not visited[n]:
          INDEG[n] -= 1 # indegree 수정
          heappush(pset, [INDEG[n], n, OUT[n]]) # 수정된 정보로 다시 heappush
      ans.append(cur)
print(*ans)