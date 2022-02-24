#dp + DFS
# dp[i] = node[i]를 고를때 최대 값
# 최대한 많은 node를 고르는 것이 정답
import sys
from collections import defaultdict
sys.setrecursionlimit(10 ** 7)
def input(): return sys.stdin.readline().rstrip()


nodes = int(input())
vals = list(map(int, input().split())) #가중치
vals.insert(0, 0) #dummy value
tree = defaultdict(list) #{key(노드) : [value] (노드와 연결된 다른노드들)}

check = [0] * (nodes + 1)
dp = [[-1, -1] for i in range(nodes+ 1)] #call by reference 주의
for i in range(nodes - 1):
  nodeX, nodeY = list(map(int, input().split()))
  tree[nodeX].append(nodeY)
  tree[nodeY].append(nodeX)

def change(res, cur, isVisited):
  dp[cur][isVisited] = res #dp[node][0] = node가 포함되지 않는 경우의 최대값
                          #dp[node][1] = node가 포함되는 경우의 최대값 /


visited = [0] * (nodes + 1)

def DynamicProgramming(cur, prev):
  dp[cur][1] = vals[cur] 
  dp[cur][0] = 0
  visited[cur] = 1
  for nextnode in tree[cur]:  # 자식노드 탐색, #자식visited = [0] * (nodes + 1)노드가 없는 경우 for문이 종료됨
    if nextnode != prev:
      DynamicProgramming(nextnode, cur)
      dp[cur][1] += dp[nextnode][0] #cur을 탐색했음 / 
      dp[cur][0] += max(dp[nextnode][0], dp[nextnode][1])


def findRoute(cur, prev, isVisited):
  if isVisited:
    answr.append(cur)
    for nextnode in tree[cur]:
      if nextnode != prev:
        findRoute(nextnode, cur, 0)  # 현재 노드를 포함했을때 이므로 그 다음 자식노드는 포함하지 못함
  else:
    for nextnode in tree[cur]:
      if nextnode != prev:
        if dp[nextnode][0] > dp[nextnode][1]:
          findRoute(nextnode, cur, 0)
        else:
          findRoute(nextnode, cur, 1)


DynamicProgramming(1, -1) #dp안을 채워주는 용도
answr = []
if dp[1][0] > dp[1][1]:
  findRoute(1, -1, 0)
else:
  findRoute(1, -1, 1)
answr.sort()
print(dp[1][0]) if dp[1][0] > dp[1][1] else print(dp[1][1])
print(*answr)

# def DynamicProgramming(visited, selected, current):
#   if selected == nodes + 1: #더 이상 고를 수 있는 node가 없을 때

#     return vals[current]
#   if dp[current] != -1: #해당 node의 dp가 존재할 때
#     return dp[current]
#   #노드 선택
#   dp[current] = -1
#   for nextnode in range(1, nodes):
#     if visited[nextnode] < 1:
#       visited[nextnode] += 1
#       cnt = 0
#       for nearby in graph[nextnode]:
#         if not visited[nearby]:
#           cnt += 1 #선택할 수 없는 인접노드 개수 계산
#         visited[nearby] += 1 #선택할 수 없는 인접노드 marking
#       dp[current] = max(vals[current] + DynamicProgramming(visited, selected + 1 + cnt, nextnode), dp[current])
#       visited[nextnode] -= 1
#       for nearby in graph[nextnode]:
#         visited[nearby] -= 1
#   return dp[current]
# #(10, 30, 40, 10, 20, 20, 70)
# DynamicProgramming(visited, 0, 0)
# print(dp[0])

#1357 7135 다 같은 노드...
# def DFS(graph, visited, independent, check, current, nodeset, memo):
#   global ans
#   if sum(check) == nodes:
#     if ans < independent:
#       ans = independent
#       for node in nodeset:
#         memo[node] = ans
#     return
#   if memo[current] != -1:
#     return memo
  
  
#   for i in range(1, nodes + 1):
#     if visited[i] < 1:
#       visited[i] += 1
#       check[i] = 1
#       for nearby in graph[i]:
#         visited[nearby] += 1
#         check[nearby] = 1
#       DFS(graph, visited, independent + vals[i], check, i, nodeset + [i], memo)
#       visited[i] -= 1
#       if visited[i] == 0:
#         check[i] = 0
#       for nearby in graph[i]:
#         visited[nearby] -= 1
#         if visited[nearby] == 0:
#           check[nearby] = 0


# DFS(graph, visited, 0, check, 1, [], memo)
# print(ans)
