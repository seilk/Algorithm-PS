import sys
sys.setrecursionlimit(10**5)
def TOP_DOWN(node):
  if not grp[node]: # 더이상 부모노드가 없을 때
    dpTABLE[node] = val[node]
    return dpTABLE[node]
  if dpTABLE[node] >= 0: # 기록된 값이 있을 때
    return dpTABLE[node]
  MAX = 0
  for new_node in grp[node]:
    MAX = max(MAX, TOP_DOWN(new_node))
  dpTABLE[node] = val[node] + MAX
  return dpTABLE[node]

In = lambda : sys.stdin.readline().rstrip()
MIS = lambda : map(int, In().split())
T = int(In())
for t in range(T):
  N, R = MIS()
  val = [0]+[*MIS()]
  grp = [[] for i in range(N+1)]
  check = [0]*(N+1)
  for r in range(R):
    a,b = MIS()
    grp[b].append(a)
  TARGET_NODE = int(In())
  dpTABLE = [-1]*(N+1)
  check = [0]*(N+1)
  TOP_DOWN(TARGET_NODE)
  if grp[TARGET_NODE]:
    print(val[TARGET_NODE] + max(dpTABLE[i] for i in grp[TARGET_NODE]))
  else:
    print(val[TARGET_NODE])