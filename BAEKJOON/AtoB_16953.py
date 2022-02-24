import sys
from collections import deque
input = sys.stdin.readline
a, b = map(int, input().split())
queue = deque([(a, 0)])
# visited 메모리 초과 원인! (크기 = 1억 이상)


def BFS():
  global minn
  while queue:
    val, cnt = queue.popleft()
    if val > b:
      continue
    if val == b:
      minn = min(minn, cnt)
      continue
    for i in range(2):
      if i == 0:
        k = val * 2

      elif i == 1:
        k = int(str(val) + "1")

      queue.append((k, cnt + 1))


minn = 9876543210
BFS()
print(-1) if minn == 9876543210 else print(minn + 1)
