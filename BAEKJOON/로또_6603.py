import sys
from collections import defaultdict
input = sys.stdin.readline


def DFS(arr, depth, visited, ans):
  if depth == 6:
    key = "".join(visited) #0101001
    if check[key] == 0:
      check[key] += 1
      print(*ans)
    return

  for i in range(len(arr)):
    if visited[i] == '0':
      ans.append(arr[i])
      visited[i] = '1'
      DFS(arr, depth + 1, visited, ans)
      visited[i] = '0'
      ans.pop()
  return

while 1:
  try:
    tmp = list(map(int, input().split()))
    visited = ['0' for i in range(tmp[0])]
    ans = []
    check = defaultdict(int)
    DFS(sorted(tmp[1:]), 0, visited, ans)
    print()
  except:
    sys.exit(0)