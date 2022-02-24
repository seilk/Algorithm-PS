import sys
from collections import deque
from heapq import heappop, heappush

input = sys.stdin.readline
print = sys.stdout.write
N, L = map(int, input().split())
arr = [None] + [*map(int, input().split())]
dq = deque([])

for i in range(1, N + 1):
  if dq:
    if dq[0][1] < i - L + 1:
      dq.popleft()
  while dq and dq[-1][0] > arr[i]:
    dq.pop()
  dq.append((arr[i], i))
  print("%s " % dq[0][0]) if i != N else print("%s " % dq[0][0]) # stdout으로 정수를 출력하는 방법 확실히 빠름!
